for bsequence in *.sam


do
	samtools view -b $bsequence|samtools sort -o sorted_${bsequence}.bam 

done