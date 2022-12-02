import scanpy as sc
# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()
newadata = sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=True)
sc.tl.pca(adata)
sc.pl.pca(adata,save='PCA plot before filtering',color_map = 'magma')
sc.tl.pca(newadata)
sc.pl.pca(newadata,save='PCA plot after filtering')
sc.pp.neighbors(newadata)
sc.tl.leiden(newadata)
tsnedata = sc.tl.tsne(newadata,copy = True)
sc.pl.tsne(tsnedata, color = 'leiden', save='t-SNE for filtered data')
umapdata = sc.tl.umap(newadata, maxiter=1000,copy = True)
sc.pl.tsne(tsnedata, color=['leiden','Mfap4','Gdpd2','P4ha3','Slc38a5','Vwf','Kcnj8','Abcc9','Vtn','C1qb','Olig2','Tyrobp','Rgs5','Ramp2'],
	save='Tsne with signature genes,for flitered data')
sc.pl.umap(umapdata, color='leiden',save='Umap for flitered data')
sc.pl.umap(umapdata, color=['leiden','Mfap4','Gdpd2','P4ha3','Slc38a5','Vwf','Kcnj8','Abcc9','Vtn','C1qb','Olig2','Tyrobp','Rgs5','Ramp2'],
	save='Umap with signature genes,for flitered data')
logregdata = sc.tl.rank_genes_groups(newadata, 'leiden', method='logreg',copy = True)
sc.pl.rank_genes_groups(logregdata, save='linear_regression_distinguished_clusters')
ttestdata = sc.tl.rank_genes_groups(newadata, 'leiden', method='t-test',copy = True)
sc.pl.rank_genes_groups(ttestdata, save='t_test_distinguished_clusters')
# var_names = {'EC':['Hbb-bs','Hba-a1','Hba-a2','Hbb-bt']}
sc.pl.rank_genes_groups_dotplot(ttestdata,save='cluster_ttest for flitered data')
sc.pl.rank_genes_groups_dotplot(logregdata,save='cluster_logreg for flitered data')

sc.pl.rank_genes_groups_stacked_violin(ttestdata,save='cluster_ttest for flitered data')
sc.pl.rank_genes_groups_stacked_violin(logregdata,save='cluster_logreg for flitered data')
marker_genes_dict = {
    'Fibroblasts': ['Mfap4'],
    'Astrocytes': ['Gdpd2', 'P4ha3'],
    'vescular ECs': ['Slc38a5','Vwf'],
    'Pericytes': ['Kcnj8', 'Abcc9' ,'Vtn'],
    'ECs type3': ['Ramp2'],
    'Microglias': ['C1qb','Tyrobp'],
    'Oligodendrocytes': ['Olig2'],
}
cluster2annotation = {
     '5': 'Astrocytes',
     '8': 'Fibroblasts',
     '21': 'Oligodendrocytes',
     '23': 'vescular ECs',
     '24': 'ECs type3',
     '25': 'Pericytes',
     '26': 'Microglias'

}
sc.pl.dotplot(umapdata, marker_genes_dict, 'leiden', save='dotplot with annotation',dendrogram=True)
umapdata.obs['cell type'] = umapdata.obs['leiden'].map(cluster2annotation).astype('category')
sc.pl.umap(umapdata, color='cell type', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2,save='umap with clustering')
# logreg = sc.tl.rank_genes_groups(newadata, 'leiden', method='logreg',copy=True)
# sc.pl.rank_genes_groups(logreg, save='linear_regression_distinguished_clusters')
# ttest = sc.tl.rank_genes_groups(newadata, 'leiden', method='t-test',copy=True)
# sc.pl.rank_genes_groups(ttest, save='t_test_distinguished_clusters')
# sc.pp.filter_genes(adata, min_counts=1)
# sc.pp.normalize_per_cell(adata, key_n_counts='n_counts_all')
# filter_result = sc.pp.filter_genes_dispersion(adata.X, 
# 	flavor='cell_ranger', n_top_genes=n_top_genes, log=False)
# adata = adata[:, filter_result.gene_subset]
# sc.pp.normalize_per_cell(adata)
# if log: sc.pp.log1p(adata)  
# sc.pp.scale(adata)