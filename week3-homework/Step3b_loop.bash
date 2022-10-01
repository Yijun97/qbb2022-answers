
for sortedsequence in *.bam
do
	samtools index -b $sortedsequence ${sortedsequence}.bai

done