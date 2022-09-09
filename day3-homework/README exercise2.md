# QBB2022 - Day 3 - Homework Exercises Submission

(testacc.eigenvec is produced from Exercise1)
Exercise 2:
the code:

‘import matplotlib.pyplot as plt’
‘import numpy as np’

‘pca = np.genfromtxt("testacc.eigenvec", dtype = None, encoding = None,’
	                            ‘names = ["position","chrom","PCA1", "PCA2", "PCA3"])’


‘fig, ax = plt.subplots()’
‘ax.scatter(pca["PCA1"], pca["PCA2"], label = "PCA1_vs_PCA2")’
‘ax.set_xlabel("pca1")’
’ax.set_ylabel("pca2")‘
‘plt.savefig("ex_a.png")’

’fig, ax = plt.subplots()’
‘ax.scatter(pca["PCA1"], pca["PCA3"], label = "PCA1_vs_PCA3")’
’ax.set_xlabel("pca1")‘
‘ax.set_ylabel("pca3")’
’plt.savefig("ex_b.png")’


‘plt.show()‘

Among the points, I notice that more data dots have positive PCA3 than  positive PCA2 when their PCA1 is near 0. Meanwhile, when PCA1 is near 0, which means PCA1 has less impact on the data, PCA3 is more evenly attributed along its axis, while PCA2 is more likely to be seperated. This means if PCA1 is not considered, PCA2 is a more important factor in affecting data distribution.

The  PCA1/PCA2 could separate  superpopulation better 





