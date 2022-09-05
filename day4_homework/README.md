# QBB2022 - Day 4 - Homework Exercises Submission

A – Expand simulation conditions

#Take a moment to use manual pages and print() statements to break this line down, recording observations and conclusions in your README.md file .
The code writes like 

'for i in range(len(tosses)):#to see how the power changes with the prob
    power = []
    for j in range(len(probs)):
        spower = run_experiment(probs[j], tosses[i], correct_the_pvalues = True)
        power.append(spower)
    print("the power for " + str(tosses[i]) + " tosses is " )
    print(power)


for i in range(len(probs)):#to see how the power changes with the tosses controlling how unfair the coin is
    power = []
    for j in range(len(tosses)):
        spower = run_experiment(probs[i], tosses[j], correct_the_pvalues = True)
        power.append(spower)
    print("the power for " + str(probs[i]) + " prob is " )
    print(power)'	
And the results show:
the power for 10 tosses is 
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
the power for 50 tosses is 
[1.0, 1.0, 1.0, 0.98, 0.87, 0.55, 0.21, 0.08, 0.02, 0.0]
the power for 100 tosses is 
[1.0, 1.0, 1.0, 1.0, 0.99, 0.95, 0.74, 0.35, 0.08, 0.01]
the power for 250 tosses is 
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.94, 0.35, 0.03]
the power for 500 tosses is 
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.85, 0.06]
the power for 1000 tosses is 
[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.34]
the power for 1.0 prob is 
[0.0, 1.0, 1.0, 1.0, 1.0, 1.0]
the power for 0.95 prob is 
[0.0, 1.0, 1.0, 1.0, 1.0, 1.0]
the power for 0.9 prob is 
[0.0, 1.0, 1.0, 1.0, 1.0, 1.0]
the power for 0.85 prob is 
[0.0, 0.98, 1.0, 1.0, 1.0, 1.0]
the power for 0.8 prob is 
[0.0, 0.87, 0.99, 1.0, 1.0, 1.0]
the power for 0.75 prob is 
[0.0, 0.55, 0.95, 1.0, 1.0, 1.0]
the power for 0.7 prob is 
[0.0, 0.21, 0.74, 1.0, 1.0, 1.0]
the power for 0.65 prob is 
[0.0, 0.08, 0.35, 0.94, 1.0, 1.0]
the power for 0.6 prob is 
[0.0, 0.02, 0.08, 0.35, 0.85, 1.0]
the power for 0.55 prob is 
[0.0, 0.0, 0.01, 0.03, 0.06, 0.34]

My conclusion: for given tosses, the more unfair the coin is, the bigger power  we will get; for given unfairness of coin, the bigger the tosses are, the bigger power we will get. This means high probs and more tosses help improve true positive rate.

# Based on the manual page, what are 0.55, 1.05, and 0.05 being used for? 
0.05 is the start value,  1.05 is the stop value which will not be included, 0.05 is the step value which is used to space the start and stop values.
print(numpy.arange(0.55, 1.05, 0.05)), I got:
[0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]. This is an array which contains decimal point.

#what should numpy.around( ,decimals=2) be doing?  How the numpy.arange(0.55, 1.05, 0.05) result changes when it is passed to numpy.around(). 
numpy.around( ,decimals=2) is used to make the array evenly round to 2 decimals.
print(numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)), I got:
0.55 0.6  0.65 0.7  0.75 0.8  0.85 0.9  0.95 1.  ]. I didn't see any changes in fact...

#Finally, focus on the [::-1] part of the code. Use a print() statement to see how the array has changed.
print(numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1])
I got:[1.   0.95 0.9  0.85 0.8  0.75 0.7  0.65 0.6  0.55]
this array is reversed.

B – Compute and store power


#Create a numpy 2-dimensional array (or matrix) where you will store the power of experiment
the code:
powermatrix = numpy.zeros((len(probs), len(tosses))) #to store the power for each toss, each possibility in a matrix
for i, prob in enumerate(probs):
    for j,toss in enumerate(tosses):
        powermatrix[i,j] = run_experiment(probs[i], tosses[j], correct_the_pvalues = True)
print(powermatrix)

the result:(each column is a different toss, each line is a different possibility)
[[0.   1.   1.   1.   1.   1.  ]
 [0.   1.   1.   1.   1.   1.  ]
 [0.   1.   1.   1.   1.   1.  ]
 [0.   0.98 1.   1.   1.   1.  ]
 [0.   0.87 0.99 1.   1.   1.  ]
 [0.   0.55 0.95 1.   1.   1.  ]
 [0.   0.21 0.74 1.   1.   1.  ]
 [0.   0.08 0.35 0.94 1.   1.  ]
 [0.   0.02 0.08 0.35 0.85 1.  ]
 [0.   0.   0.01 0.03 0.06 0.34]]

C – Plot

#Use Matplotlib and Seaborn to visualize the power for the unfair coin toss experiments within a heatmap.

Power is a probability. Therefore, I set vmin = 0 and vmax = 1;
We can set the colormap that the heatmap function will use to plot with the cmap argument.
Generally, using hue variation to represent categories. However,hue variations are not well suited to representing numeric data. Varying luminance helps us see structure in data, and changes in luminance are more intuitively processed as changes in importance. colorblind is kind of the matplotlib's palette. Seaborn in fact has six variations of matplotlib’s palette, called deep, muted, pastel, bright, dark, and colorblind. These span a range of average luminance and saturation values, which can be helpful for estimating how the the seaborn color palettes perform when simulating different forms of colorblindess.

Code:

'fig, ax = plt.subplots()
xticklabels = tosses
yticklabels = probs
camp = sns.cubehelix_palette(as_cmap=True) #use a cubehelix palettes to visualize
ax = sns.heatmap(powermatrix,vmin = 0, vmax = 1,cmap=camp, xticklabels = xticklabels, yticklabels = yticklabels)
ax.set_xlabel("tosses")
ax.set_ylabel("probability of head")
ax.set_title("The power for n_tosses and head_probability")
plt.savefig("heatmap for power")
plt.show()'

From the generated picture, I observed the color has highest density in upper right. This mean with higer tosses and higher head probability, the power will be greater.


#Make a plot that displays power, computed without Multiple Hypothesis Testing Correction and a plot that displays power with Multiple Hypothesis Testing Correction. 
the code for plot without multiple hypothesis testing:

'powermatrix = numpy.zeros((len(probs), len(tosses))) 
for i, prob in enumerate(probs):
    for j,toss in enumerate(tosses):
        powermatrix[i,j] = run_experiment(probs[i], tosses[j])

fig, ax = plt.subplots()
xticklabels = tosses
yticklabels = probs
camp = sns.cubehelix_palette(as_cmap=True) #use a cubehelix palettes to visualize
ax = sns.heatmap(powermatrix,vmin = 0, vmax = 1,cmap=camp, xticklabels = xticklabels, yticklabels = yticklabels)
ax.set_xlabel("tosses")
ax.set_ylabel("probability of head")
ax.set_title("The power for n_tosses and head_probability_without MHTC")
plt.savefig("heatmap for power_without MHTC")
plt.show()'

the code for plot with multiple hypothesis testing:

'powermatrix = numpy.zeros((len(probs), len(tosses))) 
for i, prob in enumerate(probs):
    for j,toss in enumerate(tosses):
        powermatrix[i,j] = run_experiment(probs[i], tosses[j], correct_the_pvalues = True)
    
fig, ax = plt.subplots()
xticklabels = tosses
yticklabels = probs
camp = sns.cubehelix_palette(as_cmap=True) #use a cubehelix palettes to visualize
ax = sns.heatmap(powermatrix,vmin = 0, vmax = 1,cmap=camp, xticklabels = xticklabels, yticklabels = yticklabels)
ax.set_xlabel("tosses")
ax.set_ylabel("probability of head")
ax.set_title("The power for n_tosses and head_probability_with MHTC")
plt.savefig("heatmap for power_with MHTC")
plt.show()'


D – Compare to a real study
#In your README.md file, comment on how this simulation relates to a real simulation performed recently by the McCoy lab (specifically grad student Sara Carioscia).

#Briefly summarize the biological phenomenon of interest that this study is focusing on.

This study is interested in the phenomenon that some selfish alleles have disproportionately transmission rate to the next generation. But such transmission distortion (TD) in human remains unclear for there are no reliable methods to detect small variation.

# compare the simulation experiment that you performed with the simulation experiment performed for Figure S13.
Similarity: 
1. We both applied heatmap to represent the power of a number of sperm and a certain transmission rate. 
2. We both make two plots, one has computed the multiple hypothesis testing correlation, while the other has not.  
3. Both the two plot which underwent multiple testing correlation will have less  high power.

Difference:
The p-value threshold for Fig.S13 is 1.78*10^(-7), while mine is 0.05.

More specifically, probability of heads prob_heads in my plot corresponds to the transmission rate axis, number of tosses n_tossn corresponds to the Number of sperm axis.

#Specifically, describe why both simulations use a binomial test.
The binomial test is used when an experiment has two possible outcomes (i.e. success/failure) and you have an idea about what the probability of success is. A binomial test is run to see if observed test results differ from what was expected.   In our case, we only have two possible outcomes: head or tail. And  we have an idea that the probability of success is   0.5. That's why we use a binomial test. 
  In the journal, they also have two possible outcomes: the alleles (like, A and B). And the  researche assumed that there were no transmission distortion. So they also applied a binomial test.






































