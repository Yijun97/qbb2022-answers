import sys
import math
import numpy
import numpy.matlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors

full_bed = sys.argv[1]
data = numpy.loadtxt(full_bed, dtype=numpy.dtype([('F1', int), ('F2', int), ('score', float)]))
start_bin = 54878
end_bin = 54951
matrix =  numpy.matlib.zeros(shape = (74,74))
miniscore = 0
for k in range(len(data)):
	if data[k][0] < 54952 and data[k][0] > 54877:
		if data[k][1] < 54952 and data[k][1]> 54877:
			F1 = data[k][0] - start_bin
			F2 = data[k][1] - start_bin
			matrix[F1,F2] = math.log(data[k][2],2)
			matrix[F2,F1] = math.log(data[k][2],2)
			if matrix[F2,F1] < miniscore:
				miniscore = matrix[F2,F1]
			else: 
				miniscore = miniscore
matrix = matrix - miniscore
print(matrix)
ins_score = []
pos = []
for i in range(5, 70):
	# ins_score.append(numpy.mean(matrix[(i-5):i, i:(i+5)]))
	# pos.append(i+start_bin) 
	upscore = numpy.mean(matrix[(i - 5):i, i:(i + 5)])
	downscore = numpy.mean(matrix[(i-5):i, (i-5):i])
	ins_score.append(upscore/2 + downscore/2)
	pos.append(i+start_bin)
fig, ax = plt.subplots(2, 1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(5,6.25))
pl = ax[0].imshow(-matrix, cmap = "magma")
ax[0].set_xticks([])
ax[0].set_yticks([])
ax[0].set_title("Heatmap for 40kb resolution")
ax[0].axis('off')
# plt.margins(x=0)
ax[1].set_xlim(54878,54951)
ax[1].set_xticks([54878,54951])
ax[1].set_xticklabels([10400000,13400000])
ax[1].scatter(pos,ins_score)
# plt.subplots_adjust(left=0.15,
#                 bottom=0.1,
#                 right=1.0,
#                 top=1.0,
#                 wspace=0.4,
#                 hspace=0.0)
plt.savefig("Insulator_score")
plt.show()
# print(ins_score)
# print(matrix[(5 - 5):5, 5:(5 + 5)])
# print(matrix[0,5])