# QBB2022 - Day 5 - Lunch Exercises Submission

#Exercise 1
1.sort -t "," -k 5 -r aau1043_dnm.csv > sorted_aau1043_dnm.csv #sort by proband_id

--cut out the 5th column (proband_id) and 6th column(Phased_conbined) out, whose delimiter is ",", then grep father or mother,then extract "father" or "mother" out, and count
2.cut -d "," -f 5 -f 6 sorted_aau1043_dnm.csv | grep "mother"| cut -d "," -f 1 | uniq -c > mother_dnm.csv

3.cut -d "," -f 5 -f 6 sorted_aau1043_dnm.csv | grep "father"| cut -d "," -f 1 | uniq -c > father_dnm.csv

4.join -1 2 -2 2 father_dnm.csv mother_dnm.csv > joined_dnm_f_m.csv #generate the first joined csv, the first colmn is proband_id, the second is the number from father, the third is the number from mother

---cut out the proband_id and related father or mother age, replace the delimiter"," with " ", and sort
5.cut -d "," -f 1 -f 2 aau1043_parental_age.csv |awk '$1=$1' FS="," OFS=" "|sort -k 1 -r > sorted_father_age.csv

6.cut -d "," -f 1 -f 3 aau1043_parental_age.csv |awk '$1=$1' FS="," OFS=" "|sort -k 1 -r > sorted_mother_age.csv

---get rid of the header for further joining
7.tail -n+2 sorted_father_age.csv > noheader_sorted_father_age.csv
8.join joined_dnm_f_m.csv noheader_sorted_father_age.csv |less -S
9.tail -n+2 sorted_mother_age.csv > noheader_sorted_mother_age.csv
10.join joined_dnm_f_m.csv noheader_sorted_father_age.csv > injoin.csv

#Exercise 2
Use ordinary least squares smf.ols() to test for an association between maternal age and maternally inherited de novo mutations.

The code:
'Maternal_association = smf.ols(formula = "Maternal_number ~ 1 + Mother_age ",
                        data = mut).fit()
print(Maternal_association.summary())
print(Maternal_association.pvalues)'

The results: 
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        Maternal_number   R-squared:                       0.228
Model:                            OLS   Adj. R-squared:                  0.226
Method:                 Least Squares   F-statistic:                     116.0
Date:                Fri, 02 Sep 2022   Prob (F-statistic):           6.88e-24
Time:                        15:05:55   Log-Likelihood:                -1158.1
No. Observations:                 396   AIC:                             2320.
Df Residuals:                     394   BIC:                             2328.
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept      2.5040      0.981      2.553      0.011       0.576       4.432
Mother_age     0.3776      0.035     10.772      0.000       0.309       0.446
==============================================================================
Omnibus:                       51.143   Durbin-Watson:                   2.141
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               75.501
Skew:                           0.845   Prob(JB):                     4.03e-17
Kurtosis:                       4.310   Cond. No.                         121.
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

pvalue = 6.878208e-24, so this relationship is significant. The relationship size is 0.3776.

For the Parental, pvalue =  1.552294e-84, so this relationship is also significant. The relationship size is 1.3538.

#Plot a histogram of the number of maternal de novo mutations and paternal de novo mutations per proband on a single plot with semi-transparency 
The code:
'fig, ax = plt.subplots()
ax.hist(mut["Maternal_number"], alpha = 0.5, label = "Maternal_number")
ax.hist(mut["Paternal_number"], alpha = 0.5, label = "Paternal_number")
ax.set_xlabel("number of de novo mutations")
ax.set_ylabel("number of probands")
ax.legend()
plt.show()'

#Test whether the number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband.
I applied t-test to testfy.
The code:
'print(stats.ttest_ind(mut["Maternal_number"],mut["Paternal_number"]))'
The result:
pvalue=2.198603179308129e-264 < 0.05, 
so the number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband.

#Predict the number of paternal de novo mutations for a proband with a father who was 50.5 years old at the proband’s time of birth.
the code:
'new_data = mut[0]
new_data.fill(0)
new_data['Father_age'] = float('50.5')

print(Paternal_association.predict(new_data))'

The result:
78.018535

#Optional exercise
The code:
'Maternal_association = smf.poisson(formula = "Maternal_number ~ 1 + Mother_age ",
                        data = mut).fit()
print(Maternal_association.pvalues)
print(Maternal_association.summary())

Paternal_association = smf.poisson(formula = "Paternal_number ~ 1 + Father_age ",
                        data = mut).fit()
print(Paternal_association.pvalues)
print(Paternal_association.summary())'

#Use ordinary smf.poisson() to test for an association between maternal age and maternally inherited de novo mutations.
pvalue = 5.133524e-42, the relationship is significant, and the size is  0.0281 

#Use ordinary least squares smf.ols() to test for an association between paternal age and paternally inherited de novo mutations.
pvalue = 1.169940e-192, so the relationship is significant, and the size is  0.0241.

#Test whether the number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband.
the code: 
'print(stats.ttest_ind(mut["Maternal_number"],mut["Paternal_number"]))'
the result:pvalue=2.198603179308129e-264. So the number of maternally inherited de novo mutations per proband is significantly different than the number of paternally inherited de novo mutations per proband.


#Using the relevant Poisson regression model that you fit, predict the number of paternal de novo mutations for a proband with a father who was 40.2 years old at the proband’s time of birth
The code:
'new_data = mut[0]
new_data.fill(0)
new_data['Father_age'] = 40.2

print(Paternal_association.predict(new_data))'

The result: 63.694228