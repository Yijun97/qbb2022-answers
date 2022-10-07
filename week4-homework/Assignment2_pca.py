

import matplotlib.pyplot as plt
import numpy as np

pca = np.genfromtxt("testacc.eigenvec", dtype = None, encoding = None,
	                             names = ["FID","IID","PCA1", "PCA2", "PCA3","PCA4","PCA5","PCA6","PCA7","PCA8","PCA9","PCA10"])


fig, ax = plt.subplots()
ax.scatter(pca["PCA1"], pca["PCA2"], label = "PCA1_vs_PCA2")
ax.set_xlabel("pca1")
ax.set_ylabel("pca2")
plt.savefig("genetics_relatedness.png")



plt.show()