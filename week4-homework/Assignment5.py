
import matplotlib.pyplot as plt
import numpy as np
import math
#generate information from the quantitative association testing results
snp1 = np.genfromtxt("GS451_gwas_results.assoc.linear", dtype = None, encoding = None,
	                             names = True)
snp2 = np.genfromtxt("CB1908_gwas_results.assoc.linear", dtype = None, encoding = None,
	                             names = True)
#set up blank lists to store different sets of pvalue and their corresponding chromatin, dividing them into two groups by their pvalues
gchrom_small = []
gchrom_big = []
gpval_small = []
gpval_big = []
gsnp = []
gpos = []
fig, ax = plt.subplots()

#to assess whether the pvalue is less than 10e(-5)
for i in range(len(snp1["SNP"])):
	if snp1["TEST"][i]== "ADD":
		if -math.log(snp1["P"][i],10) > 5:
			gchrom_big.append(snp1["CHR"][i])
			gpval_big.append(-math.log(snp1["P"][i],10))
			gsnp.append(snp1["SNP"][i])
			gpos.append(snp1["BP"][i])
		else: 
			gchrom_small.append(snp1["CHR"][i])
			gpval_small.append(-math.log(snp1["P"][i],10))

#find out the most associated snp
print(gsnp[gpval_big.index(max(gpval_big))])
print(gpos[gpval_big.index(max(gpval_big))])
print(gchrom_big[gpval_big.index(max(gpval_big))])
#to plot snps that are in the same chromatin seperately, giving them different color
for i in range(1,24):
	g_p = []
	g_chrom  = []
	for j, chrom in enumerate(gchrom_small):
		if chrom  == i:
			g_p.append(gpval_small[j])
			g_chrom.append(i)
	ax.scatter(g_chrom,g_p)
#plot
ax.scatter(gchrom_big, gpval_big)
ax.set_xlabel("chromatin position")
ax.set_title("Mannhaton plot for GS451")
ax.set_ylabel("-log(pvalue,10)")
plt.axhline(5, linestyle = 'dotted',label = 'P-value = 10e-5')
ax.legend()
plt.savefig("GS451.png")

#similar scripts for the CS1908 genotypes
cchrom_small = []
cchrom_big = []
cpval_small = []
cpval_big = []
csnp = []
cpos = []

fig, ax = plt.subplots()


for i in range(len(snp2["SNP"])):
	if snp2["TEST"][i]== "ADD":
		if -math.log(snp2["P"][i],10) > 5:
			cchrom_big.append(snp2["CHR"][i])
			cpval_big.append(-math.log(snp2["P"][i],10))
			csnp.append(snp2["SNP"][i])
			cpos.append(snp2["BP"][i])
		else: 
			cchrom_small.append(snp2["CHR"][i])
			cpval_small.append(-math.log(snp2["P"][i],10))

#find out the most associated snp
print(csnp[cpval_big.index(max(cpval_big))])
print(cpos[cpval_big.index(max(cpval_big))])
print(cchrom_big[cpval_big.index(max(cpval_big))])

for i in range(1,24):
	c_p = []
	c_chrom  = []
	for j, chrom in enumerate(cchrom_small):
		if chrom  == i:
			c_p.append(cpval_small[j])
			c_chrom.append(i)
	ax.scatter(c_chrom,c_p)

ax.scatter(cchrom_big, cpval_big)
ax.scatter(cchrom_big,cpval_big)
ax.set_xlabel("chromatin position")
ax.set_ylabel("-log(pvalue,10)")
plt.axhline(5, linestyle = 'dotted',label = 'P-value = 10e-5')
ax.set_title("Mannhaton plot for CB1908")
ax.legend()
plt.savefig("CB1908.png")



plt.show()