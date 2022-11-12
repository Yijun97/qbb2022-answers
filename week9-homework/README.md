#Week9-homework
#Step2.2  
Generate a QQ plot from the p-values. We suggest using the qqplot function from statsmodels.api. Use the dist argument and scipy.stats to specify the distribution you want to compare to. By default, it compares to a normal distribution (dist = scipy.stats.t) – is this what you want? In your README.md for this assignment, please interpret your QQ plot in the context of the experiment.
The normal distribution is not what we want. Instead, we need uniformal distribution for the dist argument.
The p-value is uniformly distributed when the null hypothesis is true and all other assumptions are met. The reason for this is really the definition of alpha as the probability of a type I error. We want the probability of rejecting a true null hypothesis to be alpha, we reject when the observed p-value<𝛼,p-value<α,the only way this happens for any value of alpha is when the p-value comes from a uniform distribution. 
The assumption in our case is that "gene expression won't change will the stages", thus this is a null hypothesis, so we need to use uniform distribution.

#Step2.6
Compare the lists–what is the percentage overlap with and without sex as a covariate? We suggest defining the percentage of overlap as ((# overlapping transcripts) / (# transcripts differentially expressed by stage without sex covariate)) * 100
I run this command in bash:
'comm -12 "differential expression with only stage variant" "differential expression with stage and sex variant"'
and I get:
FBtr0346735
FBtr0337069
FBtr0084347
FBtr0303508
FBtr0302023
FBtr0084479
the total for differential expression with stage and sex variant is 81
so, the percentage = (6/81)*100 = 7.41%