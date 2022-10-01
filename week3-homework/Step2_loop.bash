
for sequence in *.fastq
do
	bwa mem -R "@RG\tID:${sequence}\tSM:${sequence}" sacCer3.fa $sequence > ${sequence}_mem-pe.sam
	
done