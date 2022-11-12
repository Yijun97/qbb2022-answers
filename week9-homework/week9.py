
import numpy as np
import numpy.lib.recfunctions as rfn
import scipy
from scipy.spatial.distance import pdist
import seaborn as sns
import numpy.matlib
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import statsmodels.api as sm
import statsmodels

import math

#Step 0 Read and Proceed the data
input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, encoding='utf-8')
col_names = list(input_arr.dtype.names)
trans_name = input_arr["t_name"]
# print(input_arr)
input_arr_new = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None, 
	encoding='utf-8', usecols = (1,2,3,4,5,6,7,8,9,10))
# print(input_arr_new)

fpkm_values_2d = rfn.structured_to_unstructured(input_arr_new, dtype=np.float)
# print(fpkm_values_2d)

mean = np.median(fpkm_values_2d, axis=1, out=None, overwrite_input=False, keepdims=False)
position = np.where(mean <= 0)
# print(position)
filtered_values = np.delete(fpkm_values_2d, position, axis=0)

transformed_data = np.log2(filtered_values+0.1)
# print(transformed_data)

#Step 1 Clustering
row_genes_clusters = scipy.cluster.hierarchy.linkage(transformed_data, method='single', metric='euclidean')
col_samples_clusters = scipy.cluster.hierarchy.linkage(transformed_data.T, method='single', metric='euclidean')
row_leaf_node_id = scipy.cluster.hierarchy.leaves_list(row_genes_clusters)
col_leaf_node_id = scipy.cluster.hierarchy.leaves_list(col_samples_clusters)
row_rearr = transformed_data[row_leaf_node_id]
col_rearr = row_rearr.T[col_leaf_node_id]

col_re_pos = np.array(col_names[1:])[col_leaf_node_id]
print(col_re_pos)

#plot the heatmap
fig,ax = plt.subplots(figsize=(10,8))
# ax = sns.heatmap(col_rearr.T,xticklabels=col_re_pos)
ax = sns.heatmap(col_rearr.T)
ax.set_xticklabels(labels=col_re_pos, fontsize= 8)
ax.set_xlabel("stages")
ax.set_ylabel("samples")
plt.tight_layout()
plt.savefig("heatmap")
plt.show()


#col_names
fig,ax = plt.subplots(figsize=(10,8))
col_re_pos = np.array(col_names[1:])[col_leaf_node_id]
# print(col_re_pos)
dn = scipy.cluster.hierarchy.dendrogram(col_samples_clusters, labels = col_re_pos)
ax.set_xlabel("stages")
plt.tight_layout()
plt.savefig("dendrogram for genes")
plt.show()


#Step 2 Differential Gene Expression
#produce p-value
sexes = []
stages = []
for sample in col_names[1:]:
	sexes.append(sample.split("_")[0])
	stages.append(sample.split("_")[1])
pvalue = []
betavalue = []
for i in range(transformed_data.shape[0]):
	list_of_tuples = []
	for j in range(len(col_names[1:])):
		list_of_tuples.append((trans_name[i],transformed_data[i,j], sexes[j], stages[j]))
	longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
	transcript = smf.ols(formula = 'fpkm ~ stage + 1', data = longdf, subset=None, drop_cols=None).fit()
	
	pvalue.append(transcript.pvalues['stage'])
	betavalue.append(transcript.params["stage"])
# print(pvalue)

#produce qqplot
fix,ax= plt.subplots()
ax = sm.qqplot(np.array(pvalue), dist = scipy.stats.uniform, line = "45", fit = True)
# ax = sm.qqplot(np.array(pvalue), dist = scipy.stats.t, line = "45", fit = True)
plt.tight_layout()
plt.savefig("qqPlot1")
plt.show()

result1 = statsmodels.stats.multitest.multipletests(pvalue, alpha=0.1, method='sidak', is_sorted=False, returnsorted=False)
diff = 0
print(result1[0])
f = open("differential expression with only stage variant",'a')
for i in range(len(result1[0])):
	if result1[0][i] == True:
		diff = diff + 1
		f.write(trans_name[i])
		f.write('\n')
print(diff)

p_sex_value = []
beta_sex_value = []
for i in range(transformed_data.shape[0]):
	list_of_tuples = []
	for j in range(len(col_names[1:])):
		list_of_tuples.append((trans_name[i],transformed_data[i,j], sexes[j], stages[j]))
	longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])
	transcript = smf.ols(formula = 'fpkm ~ stage + sex + 1', data = longdf, subset=None, drop_cols=None).fit()
	
	p_sex_value.append(transcript.pvalues['stage'])
	beta_sex_value.append(transcript.params["stage"])

unslogp = []
unsbeta = []
slogp=[]
sbeta = []
result2 = statsmodels.stats.multitest.multipletests(p_sex_value, alpha=0.1, method='sidak', is_sorted=False, returnsorted=False)
sdiff = 0
print(result2[0])
f = open("differential expression with stage and sex variant",'a')
for i in range(len(result2[0])):
	if result2[0][i] == True:
		sdiff = sdiff + 1
		f.write(trans_name[i])
		f.write('\n')

print(sdiff)
#create volcano plot
for i in range(len(p_sex_value)):
	x = -math.log(p_sex_value[i],10)
	if x > 1:
		slogp.append(x)
		sbeta.append(beta_sex_value[i])
	else:
		unslogp.append(x)
		unsbeta.append(beta_sex_value[i])
plt.scatter(unsbeta,unslogp,label='insignificant')
plt.scatter(sbeta,slogp,label='significant')
plt.tight_layout()
plt.savefig("VolcanoPlot")
plt.show()