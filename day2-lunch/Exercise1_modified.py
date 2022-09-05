#!/usr/bin/env python3

import sys # package that allows us to read in input from the command line 

def parse_bed(fname): #define a funtion, whose argument is called fname
    try: #creating a variavble called fs, which is storing the opened vcf fimes
        fs = open(fname, 'r')
    except:  #error message to the user
        raise FileNotFoundError("That file doesn’t appear to exist")
    bed = [] # stores bed file

    field_types = [str, int, int, str, float, str, int, int, str, int, str, str] # set the required types for each column
    count = 0 # set the count to record the numberr of incorrectly-formatted line
    for i, line in enumerate(fs):# loop through every line in the fname, keeping track of the line number.
        if line.startswith("#"): #skip the lines beginning with "#"
            continue
        fields = line.rstrip().split()# split each line on a tab character, so that every column is an item in the list(fields)
        fieldN = len(fields) #to get the number of total column for this line
        if fieldN < 3: # we don't want bed1 and bed2
            count = count + 1 #when meeting bed1 or bed 2, add 1 to "count"
            continue
            #print(f"Line {i} appears malformed 1", file=sys.stderr)
        elif 9 < fieldN < 12: #we also don't want bed10 and bed11
            count = count + 1 #when meeting bed10 or bed11, add 1 to "count"
            continue
        	#print(f"Line {i} appears malformed 2", file=sys.stderr)
            
        try:# Try doing this
            if fieldN == 9: #this stands for bed9
                RGB = []
                origRGB = fields[8].split(",")#split this line on ","
                for i in range(len(origRGB)):
                    RGB.append(int(origRGB[i]))

                assert len(RGB) == 3 # we believe the length should be 3, for there should be 3 integers for itemRGB entries
            elif: fieldN > 11: #this stands for bed12
               
                RGB = []
                origRGB = fields[8].split(",")#split this line on ","
                for i in range(len(origRGB)):
                    RGB.append(int(origRGB[i]))
        except: #if length isn't equal to 3
            count = count + 1 #add 1 to the "count", for this line is inproper
            continue
            #print(f"Line {i} appears malformed 3", file=sys.stdeer)

        try: #Try doing this
            if fieldN > 11: #this stands for bed12
                blocksize = fields[10].rstrip(",").split(",") #split this line on ",", for there will be an additinal comma on the end
                # which will produce an unwanted space elemnt, so we strip the "," on the right side
                blockstart = fields[11].rstrip(",").split(",") #same stratege as above

                assert len(blockstart)  ==  int(fields[9]) 
                assert len(blocksize)  ==  int(fields[9]) #these three number should be equal
        except: #if not, this  line is inproper, we should add 1  to the count
            count = count + 1
            continue
            #print(f"Line {i} has umatched blocksize and blockstart", file=sys.stderr)

        try: #Try doing this
            for j in range(min(len(field_types), len(fields))): #we only do this in certain range, which should be no more than the length of datatype or the number of columns in a field
                if fields[j] != ".": #to skip the column in the fields which is "."
                    a = field_types[j](fields[j])
                    fields[j] = a #to convert the string into the data type we want
            
            bed.append(fields) #add the formatted fields into bed
        except: #if j is out of range, there should be a mistake
            continue
            count = count + 1
            #print(f"Line {i} appears malformed 4", file=sys.stderr)
    print(count) #print out the total number of incorrect of malformed entries

    fs.close()
    return bed #this is what we want: a formatted bed file


if __name__ == "__main__":
    fname = sys.argv[1]
    bed = parse_bed(fname)
