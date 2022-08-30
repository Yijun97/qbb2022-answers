
# Online Python - IDE, Editor, Compiler, Interpreter

#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys #import sys
filename = sys.argv[1] #Extracr the file name
list1 = [] #creat a list for each line

#determine the number of printed lines
if len(sys.argv) > 2: 
  desired = int(sys.argv[2])
else: 
  desired = 10 
  
#add the lines in to the list with their position information
for line in open(filename): 
  list1.append(line)
 
list1.reverse() #reverse the list to  get the  required lines
list1 = list1[:desired] #extract the list
list1.reverse() #reverse again to get the right order

for element in list1: #print the lines

        print(element)

# This is a great script. It's clear and concise. Two comments about readability.
# First, comments!!! While a small script like this is easy to follow, it's a
# habit that needs to be formed for you and others to follow your logic. Second,
# use blank lines to break up your script into blocks of functional code. You do
# this in the second part of the script, but the first part is hard to read.
# I like that you used a second reverse to put the lines back into the original
# order. Alternatively, you could use the indexing [-desired:] to get the last
# "desired" number of lines and you wouldn't need any reverses. Overall, great
# job! - Mike