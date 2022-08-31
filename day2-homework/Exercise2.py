import Exercise1 #import the Exercise1.py to get the vcf parser for random.snippet.vcf
import newvcf # import the newvcf.py to get the vcf parser for dbDNP_snippet.vcf
import sys # package that allows us to read in input from the command line 
random = sys.argv[1] #get random.snippet.vcf
dbSNP = sys.argv[2] #get dbDNP_snippet.vcf
vcfrandom = Exercise1.parse_vcf(random) #convert the random_snippet.vcf into the format we want
vcfdbSNP = newvcf.parse_vcf(dbSNP) #convert the dbSNP_snippet.vcf into the format we want
#matched = 0 #set the variable to record the number of labeled records
for randomline in vcfrandom: #read each line of vcfrandom
	rdpos = randomline[1] # use rdpos to record the position of this variant for future use
	for dbline in vcfdbSNP: #for each line of vcfrandom, I hope to compare it with the whole vcfdbSNP to see if they are matched
		dbpos = dbline[1] # use dbpos to record the position of the IDs
		if rdpos == dbpos: #check if there is a match between the two position
			randomline[2] = dbline[2] #if they are matched, replace the ID of randomline with the ID of dbline
			#matched += 1 , I am noot so sure why this "matched" cannot work, for it would add 1 each time, no matter whether the two pos matched.
		#else : #if the position of this randomline is not matched with any lines in vcfdbSNP
			#unmatched += 1 #add 1 to the record
#when the for loop ends, I should have compared all lines in vcfrandom with vcfdbSNP and replaced their IDs, and also record the number of unmatched lines in vcfrandom
#print(matched) #print the record
total = len(vcfrandom)
#unmatched = total - matched
#print(unmatched)
list = [] #create a list to  store  the ID  information from changed vcfrandom.
num = 0 # set the num to record the number of "."
#add the ID information of each line into list
for i in range(total): #each line should  be examined and added
	list.append(vcfrandom[i][2]) #extract ID information
for element in list: #to examine each element in list
	if element == ".":
		num += 1
print(num) #this is the number for ".", which stands for number of unmatched lines

