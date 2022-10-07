import sys
import matplotlib.pyplot as plt
import vcfParser
import numpy as np
# INPUT genotypes.vcf from commands
fname = sys.argv[1]
ref = []
het = []
alt = []
IC50_r = []
IC50_h = []
IC50_a = []
vcf = vcfParser.parse_vcf(fname)
#identify the most related snp, which is determined in previous steps
for i in range(len(vcf)):
	if vcf[i][2] == 'rs7257475':
		snp = vcf[i]

#found out the FID for different genotypes: alt, ref or het
for i in range(len(snp)):
	if snp[i] == "0/1" or snp[i] == "1/0" :
		het.append(vcf[0][i].split("_")[0])
	if snp[i] == "1/1":
		alt.append(vcf[0][i].split("_")[0])		
	if snp[i] == "0/0":
		ref.append(vcf[0][i].split("_")[0])
	if snp[i] == "./." :
		continue
# print(het)
#impoort the phenotype data and classify them by genotypes
ic = np.genfromtxt("gwas_data/GS451_IC50.txt", dtype = None, encoding = None, names = True)

for i in range(len(ic["FID"])):
	if str(ic["FID"][i]) in het:
		if ic["GS451_IC50"][i] == 'NA':
			continue
		IC50_h.append(float(ic["GS451_IC50"][i]))
	if str(ic["FID"][i]) in ref:
		if ic["GS451_IC50"][i] == 'NA':
			continue
		IC50_r.append(float(ic["GS451_IC50"][i]))
	if str(ic["FID"][i]) in alt:
		if ic["GS451_IC50"][i] == 'NA':
			continue
		IC50_a.append(float(ic["GS451_IC50"][i]))
print(IC50_a)
print(IC50_h)
print(IC50_r)

labels = 'alt','het','ref'
plt.boxplot([IC50_a,IC50_h,IC50_r], labels = labels, notch=None, vert=None, patch_artist=None, widths=None)

plt.xlabel("genotype")
plt.ylabel("IC50")
plt.title("Effect size for rs7257475 in GS451")
plt.savefig("Effect size for rs7257475 in GS451.png")
plt.show()
