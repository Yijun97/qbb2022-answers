#!/usr/bin/env python3

import sys # package that allows us to read in input from the command line (ex: vcf files)

def parse_vcf(fname): # defineing aa new function called parse_vcf and it takes an argument called "fname"
    vcf = [] # create an empty list  called "vcf" to store the VCF information
    info_description = {} # create an empty dictionary
    info_type = {} # create an empty dictionary
    format_description = {} # create an empty dictionary
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }  # allows us to convert information from the header to tell python what data type to express
    malformed = 0 #initialize variable to count number of malformed VCF lines

    #trying to open the VCF file; if it doesn't work, the the user
    try: 
        fs = open(fname) #creating a variavble called fs, which is storing the opened vcf fimes
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr) #error message to the user

    for h, line in enumerate(fs): # loop through every line in the vcf file, keeping track of the line number.
        if line.startswith("#"): #for header lines only
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        else: # if we are NOT on a header line, do  this:
            try: # Try doing ALL of this
                #fields is a list that stores the info in onee line of the VCF.
                fields = line.rstrip().split("\t") # split each line on a tab character, so that every colum is an item in thee list(fields)
                fields[1] = int(fields[1]) #convert the SNP position into an integer(if it doesn't work, we will automatically go to the "except" part)
                if fields[5] != ".": #if the quality is not empty, convert it into a decimal
                    fields[5] = float(fields[5]) #convert it into a decimal
                info = {} #making a disctionary to store the information in the INFO column - lines 76-83 are going to be about parsing the INFO column
                # we want the info dictionary to look like this: {"AC":91, "AN":5096,...,"NS":2548}
                for entry in fields[7].split(";"): #the list looks like["AC=91", "AN=5096", ..., "NS=2548"]
                    temp = entry.split("=") # the first entry we're working with is "AC=91", temp is a list. for the first, temp=["AC","91"]
                    if len(temp) == 1: #if there's only one item in the temp list,  what we want to do is  update the dictionary so that we know that AC has no value for this SNP 
                        info[temp[0]] = None #temp[0] is "AC", we  are adding   "AC" to the dictionary
                        #dictionaries have keys and values. You add info to a dictionary by doing dict_name[new_key] = new_value. Ex:info["AC"]= "91"
                    else: #otherwise, the INFO  field  is not empty and we're good
                        name, value = temp #temp = ["AC","91"]. name = "AC", value = "91". Another version: name = temp[0];value = temp[1]
                        # in these next two lines, we're converting the data in each entry to its correct data type. This data type was specified in the header section that we parsed above
                        Type = info_type[name] # here, we are getting the python function for data type conversion that corresponds to what the entry should be.
                        # ex, Type = info_type["AC"]
                        info[name] = type_map[Type](value)#here,we are getting the python function for converting the entry to the correct data type
                fields[7] = info #replace  the 8th item of the "fields" list with the info dictionary we just make
                if len(fields) > 8: #if we still have more columns after the INFO column, then we still have more stuff to do:
                    #Example of the format: GT:DP:AF:BG:RU
                    fields[8] = fields[8].split(":") #we are splitting the FORMAT column by ":"
                    if len(fields[8]) > 1: #if there are multiple things in the FORMAT column, we should deal with all of them individually:
                        #GT:DP, HG00097: 0|0:0.3
                        for i in range(9, len(fields)): #this goes through all the columns after the FORMAT column  -> for us, this  is range(9,2513)
                            fields[i] = fields[i].split(':') #split each genotype column along a ":", 0|0:0.3 -> ["0|0", "0.3"]
                    else: #if the genotypes don't have more than one value in them
                        fields[8] = fields[8][0] #fields[8] is ["GT"] # this code  gets you fields[8] = "GT" ;# we  set the value of fields[8] to be "GT"
                vcf.append(fields) #we've finished reformatting/cleaning all of the columns; now we add this line to our VCF list. The list is storing all the information from the VCF file
                #fields is a list that contains the information for the current line   that we're working
            except: # if anything in the  try block fails, then:
                malformed += 1 # increment the "malformed" variable by 1
    # these next three lines are modifying the first line of the vcf to match information from  the header
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
        vcf[0][8] = format_description
    # if there were any malformed lines, we're going to print out the number of lines so the user knows
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
    # at the very end of running the function, return the vcf list. Give me the data back
    return vcf

if __name__ == "__main__":
    fname = sys.argv[1]
    vcf = parse_vcf(fname)
    for i in range(10):
        print(vcf[i])
