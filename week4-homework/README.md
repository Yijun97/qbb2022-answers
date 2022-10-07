#QBB-Week 4 Homework
2. using plink to perform PCA with at least 10 principal components
'plink --vcf gwas_data/genotypes.vcf --recode --out testacc --const-fid --allow-extra-chr'
'plink --allow-extra-chr --file testacc --noweb --make-bed --out testacc'
'plink --allow-extra-chr --threads 20 -bfile testacc --pca 10 --out testacc'
3. Visualize the allele frequency spectrum by plotting a histogram of allele frequencies. 
'vcftools --vcf gwas_data/genotypes.vcf  --freq --out allele_frequency'
I got a "allele_frequency.frq" file which detailed the allele frequency for each snp.

4. Using plink, perform quantitative association testing for each phenotype.
Firstly I want to uniform the format of gene ID. In genotype text, the FID and IID are seperate; but in the eigenvec file, these two fields are linked with "_".
‘awk '{$1="";print $0}'  testacc.eigenvec > testacc_no_0.eigenvec
cut -d ' ' -f 2,3,4,5,6,7,8,9,10,11,12 testacc_no_0.eigenvec|sed 's/_/ /' > formatted_testacc.eigenvec
plink -vcf gwas_data/genotypes.vcf --linear --pheno gwas_data/GS451_IC50.txt --covar formatted_testacc.eigenvec --allow-no-sex --out GS451_gwas_results
plink -vcf gwas_data/genotypes.vcf --linear --pheno gwas_data/CB1908_IC50.txt --covar formatted_testacc.eigenvec --allow-no-sex --out CB1908_gwas_results’
5. using the file produced from 4 to draw the manhaton plot. the two related files are:
GS451_gwas_results.assoc.linear and CB1908_gwas_results.assoc.linear
these two values comtain 11 pvalues for each snp, and I chose the total pvalue (marked with "ADD") to draw.

6. Choose one of the traits for which you performed GWAS. For the top associated SNP, visualize the effect size by creating a boxplot of the phenotype stratified by genotype.
see as in python script

7. Investigate the potential causal genes in the top loci associated with each of the phenotype.
for CB1908, the top loci is rs10876043, locating in chromatin 12:49190411
for GS451, the top loci is rs7257475, locating in chromatin 19:20372113
After searching this area in UCSC Genome Browser:
the potential causal gene for CB1908 is DIP2B
the potential causal gene for GS451 is ZNF826
If we don't know the reference genomes, we can do the following:
 Click the "track search" button to find Genome Browser tracks that match specific selection criteria. 