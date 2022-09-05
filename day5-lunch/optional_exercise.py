import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api  as smf
import statsmodels.api as sm
from scipy import stats

mut = np.genfromtxt("joined_id_fc_mc_fa_ma.csv", delimiter = " ",
	            dtype = None, encoding = None, 
	            names = ["Proband_ID","Paternal_number","Maternal_number","Father_age","Mother_age"])

fig, ax = plt.subplots()
ax.scatter(mut["Mother_age"], mut["Maternal_number"])
ax.set_ylabel("the count of maternal de novo mutations")
ax.set_xlabel("mother age")
ax.set_title("Relationship between mather age and the count of maternal de novo mutations", fontsize = 10)
#plt.savefig("ex2_a.png")


fig, ax = plt.subplots()
ax.scatter(mut["Father_age"], mut["Paternal_number"])
ax.set_ylabel("the count of paternal de novo mutations")
ax.set_xlabel("father age")
ax.set_title("Relationship between  father age and the count of paternal de novo mutations", fontsize = 10)
#plt.savefig("ex2_b.png")



Maternal_association = smf.poisson(formula = "Maternal_number ~ 1 + Mother_age ",
                        data = mut).fit()
print(Maternal_association.pvalues)
print(Maternal_association.summary())

Paternal_association = smf.poisson(formula = "Paternal_number ~ 1 + Father_age ",
                        data = mut).fit()
print(Paternal_association.pvalues)
print(Paternal_association.summary())

# fig, ax = plt.subplots()
# ax.hist(mut["Maternal_number"], alpha = 0.5, label = "Maternal_number")
# ax.hist(mut["Paternal_number"], alpha = 0.5, label = "Paternal_number")
# ax.set_xlabel("number of de novo mutations")
# ax.set_ylabel("number of probands")
# ax.set_title("The occurrence of different mutation number", fontsize = 10)
# ax.legend()
# plt.savefig("ex2_c.png")

# #Test whether the number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband.
print(stats.ttest_ind(mut["Maternal_number"],mut["Paternal_number"]))

new_data = mut[0]
new_data.fill(0)
new_data['Father_age'] = 40.2

print(Paternal_association.predict(new_data))

#plt.show()