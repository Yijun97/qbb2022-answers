import Exercise1

import sys
filename  = sys.argv[1]
bed  = Exercise1.parse_bed(filename) #to get formatted bed

exoncount = [] #set a list to store exoncount for each gene
for element in bed:
	exoncount.append(element[9]) #only add exon number to  the exoncount list
exoncount.sort() #sort the list
#determine the median number of the list
a = len(exoncount) #get the total length
if a%2 ==  1: #if the length is an odd number
	b =  a//2 + 1 #this is the median position
elif a%2 == 0: #if the  length is an even number
	b = a//2 #this is the median position

print(exoncount[b-1]) #print the median of exoncount based on its position