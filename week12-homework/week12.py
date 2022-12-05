import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import math
from matplotlib.lines import Line2D


#part 1 generate a list containing the allele frequency for each generation until it reaches 1 or 0.
def allele_fixed(start_allele_frequency, population_size):
	allele_frequency_each_generation = []
	i = 1
	s = np.random.binomial(2*population_size, start_allele_frequency,i)[0]
	fre = s/(2*population_size)
	fre_al = 1-fre
	allele_frequency_each_generation.append(fre)
	while  fre != 1 and fre_al != 1:
		i += 1
		# print(i)
		s = np.random.binomial(2*population_size, fre,i)[0]
		fre = s/(2*population_size)
		fre_al = 1 - fre
		allele_frequency_each_generation.append(fre)
	print(allele_frequency_each_generation)
	return allele_frequency_each_generation

#part2 plot for allele_frequency vs generation
def frequency_plot(start_allele_frequency, population_size):
	fig, ax = plt.subplots()
	allele_frequency_each_generation = allele_fixed(start_allele_frequency, population_size)
	generation = []
	for i in range(len(allele_frequency_each_generation)):
		generation.append(i+1)
	ax.plot(generation, allele_frequency_each_generation)
	ax.set_xlabel("generation")
	ax.set_ylabel("allele_frequency")
	ax.set_title('p_start = ' + str(start_allele_frequency) + ', N = ' + str(population_size))
	plt.savefig("allele frequency over generation")
	print(generation)
	plt.show()

frequency_plot(0.7, 1000)

#part 3 density plot for fix time over 1000 simulations
fixation_time = []
for i in range(1000):
	print(i)
	fixation_allele_list = allele_fixed(0.5, 100)
	fixation_time.append(len(fixation_allele_list))

fig, ax = plt.subplots()
ax.hist(fixation_time, density=True)
ax.set_xlabel("fixation time")
ax.set_ylabel("density")
ax.set_title('time to fixation over 1000 independent runs')
plt.savefig("Density of fixation time over 1000 simulations")
plt.show()


#part4 plot for fix time changing with the population size
fixation_time_population_size = []
population = [100,1000,5000,10000,50000,100000]
for N in population:
	fixation_allele_number = allele_fixed(0.5, N)
	fixation_time_population_size.append(len(fixation_allele_number))

fig, ax = plt.subplots()
ax.plot(population, fixation_time_population_size)
ax.set_ylabel("fixation time")
ax.set_xscale("log",base = 10)
ax.set_xlabel("population size")
ax.set_title('time to fixation with different population')
plt.savefig("fixation time over different population size")
plt.show()


#part5 producing the variantion plot for the fix time of each start allele frequency, where 
#      the population size is 1000, and simulates each allele frequency for 100 times.
fixation_time_start_allele_array = []
fixation_time_average = [] #store the average fixation time for each allele frequency to plot the median fixtime
allele_fre_range = [0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
for fre in allele_fre_range:
	fix_single_allele_range = []
	for i in range(100): #simulation for 100 times
		fixation_allele_fre = allele_fixed(fre, 1000)
		fix_single_allele_range.append(len(fixation_allele_fre))
	fixation_time_start_allele_array.append(fix_single_allele_range)
	average = 0
	for fix in fix_single_allele_range:
		average = average + fix
	fixation_time_average.append(average/len(fix_single_allele_range))

# #making jitter plot
fig, (ax,ax_leg) = plt.subplots(2, figsize=(12,10), gridspec_kw={'height_ratios':[6, 1]})
sns.stripplot(data=fixation_time_start_allele_array,ax = ax)
sns.scatterplot(data=fixation_time_average, marker='_', s=1000, color='k', ax=ax)
legend_elements = [Line2D([0], [0], marker='o', color='w', 
                          label='One test result', 
                          markerfacecolor='k', markersize=10),
                   Line2D([0], [0], marker='_', color='k', 
                          label='Mean quality score for the unit', 
                          linestyle='None', markersize=25)]
legend = ax_leg.legend(handles=legend_elements, loc='upper center', 
                       ncol=2, frameon=False, fontsize=12)
ax.set_xticks([0,1,2,3,4,5,6,7,8,9], allele_fre_range)
ax.set_ylabel("fixation time")
ax.set_xlabel("starting allele frequency")
ax.text(7,np.max(fixation_time_start_allele_array),'population size = 1000') #set the position
ax.set_title('Jitter plot for time to fixation with different starting allele frequency')
plt.savefig('Jitter plot for time to fixation with different starting allele frequency')
plt.show()

# #making violin plot
fig, ax = plt.subplots()
plt.violinplot(fixation_time_start_allele_array)
ax.set_xticks([0,1,2,3,4,5,6,7,8,9], allele_fre_range)
ax.set_ylabel("fixation time")
ax.set_xlabel("starting allele frequency")
ax.text(7,np.max(fixation_time_start_allele_array),'population size = 1000') #set the position
ax.set_title('Violin plot for time to fixation with different starting allele frequency')
plt.savefig('Violin plot for time to fixation with different starting allele frequency')
plt.show()

# #make the box plot 
fig, ax = plt.subplots()
plt.boxplot(fixation_time_start_allele_array)
ax.set_xticks([0,1,2,3,4,5,6,7,8,9], allele_fre_range)
ax.set_ylabel("fixation time")
ax.set_xlabel("starting allele frequency")
ax.text(7,np.max(fixation_time_start_allele_array),'population size = 1000') #set the position
ax.set_title('Boxplot for time to fixation with different starting allele frequency')
plt.savefig('Boxplot for time to fixation with different starting allele frequency')
plt.show()

















