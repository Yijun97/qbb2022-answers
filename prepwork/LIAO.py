
# Online Python - IDE, Editor, Compiler, Interpreter

#USAGE: python scriptname.py input_filename [number_lines_to_display]
import sys 
filename = sys.argv[1] 
list1 = []
if len(sys.argv) > 2: 
  desired = int(sys.argv[2])
else: 
  desired = 10 
for line in open(filename): 
  list1.append(line)
 
list1.reverse()
list1 = list1[:desired]
list1.reverse()

for element in list1:

        print(element)