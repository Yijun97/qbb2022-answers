


import matplotlib.pyplot as plt
import numpy as np

pca = np.genfromtxt("testacc.eigenvec", dtype = None, encoding = None,
	                             names = ["position","chrom","PCA1", "PCA2", "PCA3"])


fig, ax = plt.subplots()
ax.scatter(pca["PCA1"], pca["PCA2"], label = "PCA1_vs_PCA2")
ax.set_xlabel("pca1")
ax.set_ylabel("pca2")
plt.savefig("ex_a.png")

fig, ax = plt.subplots()
ax.scatter(pca["PCA1"], pca["PCA3"], label = "PCA1_vs_PCA3")
ax.set_xlabel("pca1")
ax.set_ylabel("pca3")
plt.savefig("ex_b.png")


plt.show()