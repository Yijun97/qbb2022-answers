#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt
import vcfParser
import math

DP_list = []
GQ_list = []
AF_list = []
High = 0 
Moderate = 0
Low = 0
Modifier = 0

fname = sys.argv[1]
vcf = vcfParser.parse_vcf(fname)
for i in range(1,len(vcf)):
	snp  = vcf[i]
	Effect_list = snp[7]["ANN"].split(",")
	for k in range(len(Effect_list)):
		each_effect_list = Effect_list[k].split("|")
		if each_effect_list[2] == 'HIGH':
			High += 1
		if each_effect_list[2] == 'MODERATE':
			Moderate += 1
		if each_effect_list[2] == 'LOW':
			Low += 1
		if each_effect_list[2] == 'MODIFIER':
			Modifier += 1

	AF_list.append(float(snp[7]["AF"]))
	for j in range(9,len(snp)):
		dp = snp[j][2]
		gq = snp[j][1]
		if dp == ".":
			continue
		DP_list.append(int(dp))

		if gq == ".":
			continue
		GQ_list.append(float(gq))


fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize = (12,8))
ax1=plt.subplot(2,2,1)
ax1.hist(DP_list,log = True)
ax1.set_xlabel('The Read Depth',fontsize = 8)
ax1.set_ylabel('The count of each read depth',fontsize = 8)
ax1.set_title('The Distribution of Read Depth', fontsize = 8)
ax2=plt.subplot(2,2,2)
ax2.hist(GQ_list,log = True)
ax2.set_xlabel('The Quality',fontsize = 8)
ax2.set_ylabel('The number of each quality',fontsize = 8)
ax2.set_title('The Distribution of Quality', fontsize = 8)
ax3=plt.subplot(2,2,3)
ax3.hist(AF_list)
ax3.set_xlabel('The Allele Frequency',fontsize = 8)
ax3.set_ylabel('The number of each Allele Frequncy',fontsize = 8)
ax3.set_title('The Spectrum of Allele Frequncy', fontsize = 8)
ax4=plt.subplot(2,2,4)
x = ['HIGH', 'MODERATE', 'LOW', 'MODIFIER']
y = [High, Moderate, Low, Modifier]
ax4.bar(x,y,log = True)
ax4.set_xlabel('Possible Effects',fontsize = 8)
ax4.set_ylabel('Number of each effect',fontsize = 8)
ax4.set_title('The Summary of Predicted Effects', fontsize = 8)


plt.savefig("summary plot")
plt.show()

