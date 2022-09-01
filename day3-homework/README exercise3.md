# QBB2022 - Day 3 - Homework Exercises Submission

Exercise 3
from the bash:
awk '{$1="";print $0}' testacc.eigenvec | sed -e 's/[^ ]* //'  > newtestacc.eigenvec
sort -k 1 newtestacc.eigenvec > sorted.eigenvec
 (testaccc.eigenvec is produced from Exercise 1, which contains the values for PCAs. This step is try to strip the first column, which is "0", and then sort on the genename fields for further use)
sort -k 1 integrated_call_samples.panel > sorted_samples.panel (sort another file)
join sorted.eigenvec sorted_samples.panel > sorted.text
cut -d " "  -f 5 sorted.text | sort | uniq >  population.txt (produce a text which stores the kinds of population)
cut -d " "  -f 6 sorted.text | sort | uniq >  superpopulation.txt
cut -d " "  -f 7 sorted.text | sort | uniq >  sex.txt

the code:
USAGE: python Exercise3.py population.txt superpopulation.txt sex.txt
(sorted.text is produced from the "join" work)

import matplotlib.pyplot as plt 
import numpy as np 
import sys


info = np.genfromtxt("sorted.text", dtype = None, encoding = None,
	                             names = ["genename","PCA1","PCA2", "PCA3", "Population","Superpopulation","Sex"])

(the following block is to  creat three lists to store the type information for each characteristic, thus for further analysis)
pop = []
supop = []
sex = []
for line in open(sys.argv[1]):
	cline = line.strip("\n")(the original line contains "\n")
	pop.append(cline)
for line1 in open(sys.argv[2]):
	cline1 = line1.strip("\n")
	supop.append(cline1)
for line2 in open(sys.argv[3]):
	cline2 = line2.strip("\n")
	sex.append(cline2)

fig, ax = plt.subplots() #to plot a figure

for i in range(len(pop)):  #for each type
	pca1_p = []
	pca2_p = []   ##create two lists to store  the cooridinates
	for j,element in enumerate(info["Population"]): #try to see if this genedata belongs to this subtype
		
		if element == pop[i]:
			
			pca1_p.append(info["PCA1"][j])
			pca2_p.append(info["PCA2"][j])  #append the list
	ax.scatter(pca1_p, pca2_p, label = pop[i]) #plot within this type, which will be in the same color

ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA analysis based on population groups")
ax.legend()

plt.savefig("ex3_a.png")



fig, ax = plt.subplots()
for i in range(len(supop)):
	pca1_sp = []
	pca2_sp = []
	for j,element in enumerate(info["Superpopulation"]):
		if element == supop[i]:
			
			pca1_sp.append(info["PCA1"][j])
			pca2_sp.append(info["PCA2"][j])
	ax.scatter(pca1_sp, pca2_sp, label = supop[i])

ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA analysis based on superpopulation groups")
ax.legend()

plt.savefig("ex3_b.png")

fig, ax = plt.subplots()
for i in range(len(sex)):
	pca1_s = []
	pca2_s = []
	for j,element in enumerate(info["Sex"]):
		if element == sex[i]:
			pca1_s.append(info["PCA1"][j])
			pca2_s.append(info["PCA2"][j])
	ax.scatter(pca1_s, pca2_s, label = sex[i])

ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("PCA analysis based on sex groups")
ax.legend()

plt.savefig("ex3_c.png")

		
plt.show()





