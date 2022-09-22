
from fasta import readFASTA
import numpy as np
import sys
#file input order: AA.fasta, DNA.fasta, BLOSUM62.txt, HOXD79.txt

DNA_sequences = readFASTA(open(sys.argv[2]))
DNA_1_sequence = DNA_sequences[0][1]


DNA_2_sequence = DNA_sequences[1][1]

DNA_score_matrix = []
DNA_original_score = [] #to store the information about different bases

#to produce the array for DNA scoring
for i, line in enumerate(open(sys.argv[4])):
	#to get rid of the first row and make the score string into an int, then store them in list
	if i == 0:
		cline = line.rstrip().split()
		cline.insert(0, "Nothing") #to make up one element for line 0
		DNA_original_score.append(cline)
	else:
		cline = line.rstrip().split()
		DNA_original_score.append(cline)
		scoreline = [] #get rid of the first element, which is a letter.
		for k, value in enumerate(cline):
			if k == 0:
				continue
			else:
				value = int(value)
				scoreline.append(value)
		DNA_score_matrix.append(scoreline) #produce the list of each line sublist
		DNA_score_array = np.array(DNA_score_matrix) #produce score array


#make dictionary to store the different match score
dna_dic = {}
for i in range(len(DNA_original_score)):
	if i == 0:
		continue;
	else:
		for j in range(len(DNA_original_score)):  
			if j == 0:
				continue
			else:
				my_tuple = (DNA_original_score[i][0],DNA_original_score[0][j])
				dna_dic[my_tuple] = int(DNA_original_score[i][j])


F_dna_matrix = np.zeros((len(DNA_1_sequence)+1, len(DNA_2_sequence)+1))
Trace_dna_matrix = np.zeros((len(DNA_1_sequence)+1, len(DNA_2_sequence)+1))

for i in range(len(DNA_1_sequence)+1):
	F_dna_matrix[i,0] = i*(-300)

for j in range(len(DNA_2_sequence)+1):
	F_dna_matrix[0,j] = j*(-300)

for i in range(1,len(DNA_1_sequence)+1):
	for j in range(1,len(DNA_2_sequence)+1):

		d = F_dna_matrix[i-1, j-1] + dna_dic[DNA_1_sequence[i-1],DNA_2_sequence[j-1]]
		h = F_dna_matrix[i, j-1] - 300
		v = F_dna_matrix[i-1, j] - 300
		F_dna_matrix[i,j] = max(d,h,v)
print(F_dna_matrix)
print(F_dna_matrix[len(DNA_1_sequence),len(DNA_2_sequence)])
i = F_dna_matrix.shape[0]-1
j = F_dna_matrix.shape[1]-1
while i>=1 and j>=1:
	# while j >=0:
		d = F_dna_matrix[i-1, j-1] + dna_dic[DNA_1_sequence[i-1],DNA_2_sequence[j-1]]
		h = F_dna_matrix[i, j-1] - 300
		v = F_dna_matrix[i-1, j] - 300
		if d == max(d,h,v):
			Trace_dna_matrix[i-1,j-1] = 1
			j -= 1
			i -= 1
		if h == max(d,h,v):
			Trace_dna_matrix[i,j-1] = 2
			j -= 1
		if v == max(d,h,v):
			Trace_dna_matrix[i-1,j] = 3
			i -= 1


print(Trace_dna_matrix)


DNA_align_1 = [0]*max((len(DNA_1_sequence),len(DNA_2_sequence)))
DNA_align_2 = [0]*max((len(DNA_1_sequence),len(DNA_2_sequence)))

leading_gaps = 0
trailing_gaps = 0
for i in range(len(DNA_1_sequence)+1):
	for j in range(len(DNA_2_sequence)+1):
		if Trace_dna_matrix[i,j] == 1:
			if i <= j:
				DNA_align_1[j] = DNA_1_sequence[i]
				DNA_align_2[j] = DNA_2_sequence[j]
			else:
				DNA_align_1[i] = DNA_1_sequence[i]
				DNA_align_2[i] = DNA_2_sequence[j]
		if Trace_dna_matrix[i,j] == 2:
			if i <= j:
				DNA_align_1[j] = "-"
				DNA_align_2[j] = DNA_2_sequence[j]
				leading_gaps += 1
			else:
				DNA_align_1[i] = "-"
				DNA_align_2[i] = DNA_2_sequence[j]
				leading_gaps += 1
		if Trace_dna_matrix[i,j] == 3:
			if i <= j:
				DNA_align_1[j] = DNA_1_sequence[i]
				DNA_align_2[j] = "-"
				trailing_gaps += 1
			else:
				DNA_align_1[i] = DNA_1_sequence[i]
				DNA_align_2[i] = "-"
				trailing_gaps += 1

print(DNA_align_1)
print(DNA_align_2)

with open("DNA_alignment_detail", "w") as f:
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
	f.write(str(F_dna_matrix[len(DNA_1_sequence),len(DNA_2_sequence)]))

with open("DNA_alignment", "w") as f:
	f.write("DNA_1_squence: ")
	f.write('\n')
	f.writelines(DNA_align_1)
	f.write('\n')
	f.write("DNA_2_sequence: ")
	f.write('\n')
	f.writelines(DNA_align_2)


