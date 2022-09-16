import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api  as smf
import statsmodels.api as sm
from scipy import stats
from scipy.stats import poisson

startposition_arr = np.random.randint(0, 999901, size=150000)
endposition_arr = startposition_arr + 99
position_frequency = [0]*1000000
for i in range(150000):
	for j in range(startposition_arr[i],endposition_arr[i]+1):
		position_frequency[j] += 1
max_coverage = max(position_frequency)
print(max_coverage)
count_actual = 0
for i in range(len(position_frequency)):
	if position_frequency[i] == 0:
		count_actual +=  1


fig, ax = plt.subplots()
ax.hist(position_frequency,density = True, label = 'coverage frequency')
ax.set_ylabel("the frequency of the coverage")
ax.set_xlabel("the coverage for each base")
ax.set_title("genome coverage", fontsize = 10)


probs_list=[]
for i in range(max_coverage+1):
	probs_list.append(stats.poisson.pmf(i, 15))
prob_poisson_0 = stats.poisson.pmf(0,15)
count_possion = prob_poisson_0*1000000
print(str(count_actual) + ' base pairs have 0x coverage. According to Poisson expectation, the number should be '+ str(count_possion))
ax.plot(probs_list,label = 'Poisson Probability')


plt.legend()
plt.savefig("ex1_4.png")
plt.show()



