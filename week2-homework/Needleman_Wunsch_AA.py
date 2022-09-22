
from fasta import readFASTA
import numpy as np
import sys

#file input order: AA.fasta, DNA.fasta, BLOSUM62.txt, HOXD79.txt

AA_sequences = readFASTA(open(sys.argv[1]))
AA_1_sequence = AA_sequences[0][1]


AA_2_sequence = AA_sequences[1][1]

AA_score_matrix = []
AA_original_score = [] #to store the information about different amino acids

#to produce the array for AA scoring
for i, line in enumerate(open(sys.argv[3])):
	#to get rid of the first row and make the score string into an int, then store them in list
	if i == 0:
		cline = line.rstrip().split()
		cline.insert(0, "Nothing") #to make up one element for line 0
		AA_original_score.append(cline)
	else:
		cline = line.rstrip().split()
		AA_original_score.append(cline)
		scoreline = [] #get rid of the first element, which is a letter.
		for k, value in enumerate(cline):
			if k == 0:
				continue
			else:
				value = int(value)
				scoreline.append(value)
		AA_score_matrix.append(scoreline) #produce the list of each line sublist
		AA_score_array = np.array(AA_score_matrix) #produce score array


#make dictionary to store the different match score
aa_dic = {}
for i in range(len(AA_original_score)):
	if i == 0:
		continue;
	else:
		for j in range(len(AA_original_score)):  
			if j == 0:
				continue
			else:
				my_tuple = (AA_original_score[i][0],AA_original_score[0][j])
				aa_dic[my_tuple] = int(AA_original_score[i][j])


F_aa_matrix = np.zeros((len(AA_1_sequence)+1, len(AA_2_sequence)+1))
Trace_aa_matrix = np.zeros((len(AA_1_sequence)+1, len(AA_2_sequence)+1))

for i in range(len(AA_1_sequence)+1):
	F_aa_matrix[i,0] = i*(-10)

for j in range(len(AA_2_sequence)+1):
	F_aa_matrix[0,j] = j*(-10)

for i in range(1,len(AA_1_sequence)+1):
	for j in range(1,len(AA_2_sequence)+1):

		d = F_aa_matrix[i-1, j-1] + aa_dic[AA_1_sequence[i-1],AA_2_sequence[j-1]]
		h = F_aa_matrix[i, j-1] - 10
		v = F_aa_matrix[i-1, j] - 10
		F_aa_matrix[i,j] = max(d,h,v)

print(F_aa_matrix[len(AA_1_sequence),len(AA_2_sequence)])
i = F_aa_matrix.shape[0]-1
j = F_aa_matrix.shape[1]-1
while i>=1 and j>=1:
	# while j >=0:
		d = F_aa_matrix[i-1, j-1] + aa_dic[AA_1_sequence[i-1],AA_2_sequence[j-1]]
		h = F_aa_matrix[i, j-1] - 10
		v = F_aa_matrix[i-1, j] - 10
		if d == max(d,h,v):
			Trace_aa_matrix[i-1,j-1] = 1
			j -= 1
			i -= 1
		if h == max(d,h,v):
			Trace_aa_matrix[i,j-1] = 2
			j -= 1
		if v == max(d,h,v):
			Trace_aa_matrix[i-1,j] = 3
			i -= 1

print(Trace_aa_matrix)

AA_align_1 = [0]*max((len(AA_1_sequence),len(AA_2_sequence)))
AA_align_2 = [0]*max((len(AA_1_sequence),len(AA_2_sequence)))

leading_gaps = 0
trailing_gaps = 0
for i in range(len(AA_1_sequence)+1):
	for j in range(len(AA_2_sequence)+1):
		if Trace_aa_matrix[i,j] == 1:
			if i <= j:
				AA_align_1[j] = AA_1_sequence[i]
				AA_align_2[j] = AA_2_sequence[j]
			else:
				AA_align_1[i] = AA_1_sequence[i]
				AA_align_2[i] = AA_2_sequence[j]
		if Trace_aa_matrix[i,j] == 2:
			if i <= j:
				AA_align_1[j] = "-"
				AA_align_2[j] = AA_2_sequence[j]
				leading_gaps += 1
			else:
				AA_align_1[i] = "-"
				AA_align_2[i] = AA_2_sequence[j]
				leading_gaps += 1
		if Trace_aa_matrix[i,j] == 3:
			if i <= j:
				AA_align_1[j] = AA_1_sequence[i]
				AA_align_2[j] = "-"
				trailing_gaps += 1
			else:
				AA_align_1[i] = AA_1_sequence[i]
				AA_align_2[i] = "-"
				trailing_gaps += 1

with open("AA_alignment_detail", "w") as f:
	f.write("The number of leading gaps is: ")
	f.write('\n')
	f.write(str(leading_gaps))
	f.write('\n')
	f.write("The number of trailing gaps is: ")
	f.write('\n')
	f.write(str(trailing_gaps))
	f.write('\n')
	f.write("The score of this AA alignment is: ")
	f.write('\n')
	f.write(str(F_aa_matrix[len(AA_1_sequence),len(AA_2_sequence)]))


with open("AA_alignment", "w") as f:
	f.write("AA_1_squence: ")
	f.write('\n')
	f.writelines(AA_align_1)
	f.write('\n')
	f.write("AA_2_sequence: ")
	f.write('\n')
	f.writelines(AA_align_2)

