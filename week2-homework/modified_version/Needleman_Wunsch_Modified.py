
from fasta import readFASTA
import numpy as np
import sys

#file input order:DNA/AA fasta, score.txt penalty
#file input order: AA.fasta, DNA.fasta, BLOSUM62.txt, HOXD79.txt

sequences = readFASTA(open(sys.argv[2]))
genre = str(sys.argv[1])
penalty = int(sys.argv[4])
sequence_1 = sequences[0][1]
sequence_2 = sequences[1][1]

score_matrix = []
original_score = [] #to store the information about different amino acids or nucleic acids

#to produce the array for AA scoring
for i, line in enumerate(open(sys.argv[3])):
	#to get rid of the first row and make the score string into an int, then store them in list
	if i == 0:
		cline = line.rstrip().split()
		cline.insert(0, "Nothing") #to make up one element for line 0
		original_score.append(cline)
	else:
		cline = line.rstrip().split()
		original_score.append(cline)
		scoreline = [] #get rid of the first element, which is a letter.
		for k, value in enumerate(cline):
			if k == 0:
				continue
			else:
				value = int(value)
				scoreline.append(value)
		score_matrix.append(scoreline) #produce the list of each line sublist
		score_array = np.array(score_matrix) #produce score array


#make dictionary to store the different match score
dic = {}
for i in range(len(original_score)):
	if i == 0:
		continue;
	else:
		for j in range(len(original_score)):  
			if j == 0:
				continue
			else:
				my_tuple = (original_score[i][0],original_score[0][j])
				dic[my_tuple] = int(original_score[i][j])


F_matrix = np.zeros((len(sequence_1)+1, len(sequence_2)+1))
Trace_matrix = np.zeros((len(sequence_1)+1, len(sequence_2)+1))

for i in range(len(sequence_1)+1):
	F_matrix[i,0] = i * penalty * (-1)

for j in range(len(sequence_2)+1):
	F_matrix[0,j] = j* penalty * (-1)

for i in range(1,len(sequence_1)+1):
	for j in range(1,len(sequence_2)+1):

		d = F_matrix[i-1, j-1] + dic[sequence_1[i-1],sequence_2[j-1]]
		h = F_matrix[i, j-1] - penalty
		v = F_matrix[i-1, j] - penalty
		F_matrix[i,j] = max(d,h,v)

print(F_matrix[len(sequence_1),len(sequence_2)])
i = F_matrix.shape[0]-1
j = F_matrix.shape[1]-1
align_1 = []
align_2 = []
leading_gaps = 0
trailing_gaps = 0
while i>=1 and j>=1:
	# while j >=0:
		d = F_matrix[i-1, j-1] + dic[sequence_1[i-1],sequence_2[j-1]]
		h = F_matrix[i, j-1] - penalty
		v = F_matrix[i-1, j] - penalty
		if d == max(d,h,v):
			Trace_matrix[i-1,j-1] = 1
			j -= 1
			i -= 1
			align_1.append(sequence_1[i-1])
			align_2.append(sequence_2[j-1])

		if h == max(d,h,v):
			Trace_matrix[i,j-1] = 2
			j -= 1
			align_1.append("-")
			align_2.append(sequence_2[j-1])
			leading_gaps += 1
		if v == max(d,h,v):
			Trace_matrix[i-1,j] = 3
			align_1.append(sequence_1[i-1])
			align_2.append("-")
			trailing_gaps += 1
			i -= 1

print(Trace_matrix)

name = str(genre + '_alignment_detail')
with open(name, "w") as f:
	f.write("The number of leading gaps is: ")
	f.write('\n')
	f.write(str(leading_gaps))
	f.write('\n')
	f.write("The number of trailing gaps is: ")
	f.write('\n')
	f.write(str(trailing_gaps))
	f.write('\n')
	f.write("The score of this alignment is: ")
	f.write('\n')
	f.write(str(F_matrix[len(sequence_1),len(sequence_2)]))

namealign = str(genre + '_alignment')
with open(namealign, "w") as f:
	f.write("squence_1: ")
	f.write('\n')
	f.writelines(list(reversed(align_1)))
	f.write('\n')
	f.write("sequence_2: ")
	f.write('\n')
	f.writelines(list(reversed(align_2)))

