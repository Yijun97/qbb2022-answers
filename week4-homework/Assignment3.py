import matplotlib.pyplot as plt
import numpy as np

#generate a np file from the allele frequency file, which is composed of several arrays.
snp = np.genfromtxt("allele_frequency.frq", skip_header = 1, dtype = None, encoding = None)


#generate the allele frequency list for each allele. 
allele_freq = []
for eachsnp in snp:
#for we don't know each snp has how many alleles, we need to use a for loop
	for i in range(5,len(eachsnp)):
		#the format is allele:fre, so we need to split,and the first allele is the reference allele \, which is not snp, so we need to skip.
		allele_freq_sub = float(eachsnp[i].split(":")[1])

		allele_freq.append(allele_freq_sub)
print(type(allele_freq[1]))
# print(allele_freq)
fig, ax = plt.subplots()
ax.hist(allele_freq, label= "allele frequency spectrum")
ax.set_xlabel("allele_frequency")
ax.set_ylabel("count")
ax.legend()
plt.savefig("allele_frequency_spectrum.png")



plt.show()