# Feedback day2-homework 

Your comments in the VCF parser are very detailed and complete. It appears that you understand what each block of code is doing and why. Your labeling script is less clear. It looks like you are not comfortable using dictionaries in your code yet. I understand the nested loop that you are using works, but it is going to be very slow since you will have to loop through the dbSNP list once for each item in the vcfrandom list. This is a situation where a dictionary would be ideal. If you do a single loop through your dbSNP list, you can add an entry for each ID-pos pair.

```
db_dict = {}
for dbline in vcfdbSNP:
    db_dict[dbline[1]] = dbline [2]
```

Then you can do one loop through the vcfrandom list, checking if the pos occurs in the dictionary and if it does, get the ID (the value) from it and replace the ID in that vcfrandom line. It you're still feeling uncomfortable with dictionaries, please speak to one of the instructors or TAs. Any one of us would be happy to work with you in understanding this concept. You're doing well. Keep it up!