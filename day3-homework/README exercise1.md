# QBB2022 - Day 3 - Homework Exercises Submission
Exercise 1:
'plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --recode --out testacc --const-fid --allow-extra-chr'
'plink --allow-extra-chr --file testacc --noweb --make-bed --out testacc'
'plink --allow-extra-chr --threads 20 -bfile testacc --pca 3 --out testacc'

produce 3 PCA and a .eigenvec file to store their values.