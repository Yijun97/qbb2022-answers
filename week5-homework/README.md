#QBB-Week5-homwork
#PART1
1. Filtering reads
'samtools view D2_Sox2_R1.bam -q 10 > D2_Sox2_R1.sam
samtools view D2_Sox2_R1_input.bam -q 10 > D2_Sox2_R1_input.sam
samtools view D2_Sox2_R2_input.bam -q 10 > D2_Sox2_R2_input.sam
samtools view D2_Sox2_R2.bam -q 10 > D2_Sox2_R2.sam'
2. Calling peaks
'macs2 callpeak -t D2_Sox2_R2.sam -c D2_Sox2_R2_input.sam -g 94987271 --outdir D2_Sox2_R2 -B'
'macs2 callpeak -t D2_Sox2_R1.sam -c D2_Sox2_R1_input.sam -g 94987271 --outdir D2_Sox2_R1 -B'
3. Intersecting peaks
'bedtools intersect -a D2_Sox2_R1/NA_peaks.narrowPeak -b D2_Sox2_R2/NA_peaks.narrowPeak -wa > intersect_1.bed'

4. Step 4: Colocalization of Sox2 and Klf4. Find the number of total peaks and overlapping peaks for Klf4 and Sox2 in your data. What is the percentage of Klf4 peaks colocalized with Sox2
'bedtools intersect -a intersect_1.bed -b D2_Klf4_peaks.bed|wc'
I got the result 
 41     410    2821
So, there are 40 overlapping peaks.
'wc D2_Klf4_peaks.bed'
I got "60     600    4262"
There are 60 peaks in Klf4.
Thus, 41/60 * 100% = 68.3% of the Klf4 peaks colocalized with Sox2.

5. plot
'cp ../../cmdb-quantbio/assignments/lab/ChIP-seq/extra_data/bdg_loader.py .
cp ../../cmdb-quantbio/assignments/lab/ChIP-seq/extra_data/scale_bdg.py .
python scale_bdg.py D2_Sox2_R1/NA_treat_pileup.bdg D2_Sox2_R1/Scaled_NA_treat_pileup.bdg
python scale_bdg.py D2_Klf4_treat.bdg Scaled_D2_Klf4_treat.bdg
python scale_bdg.py D0_H3K27ac_treat.bdg Scaled_D0_H3K27ac_treat.bdg
python scale_bdg.py D2_H3K27ac_treat.bdg Scaled_D2_H3K27ac_treat.bdg
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0}' Scaled_D2_Klf4_treat.bdg >  cropped_D2_Klf4_treat.bdg 
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0}' Scaled_D0_H3K27ac_treat.bdg >  cropped_D0_H3K27ac_treat.bdg 
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0}' Scaled_D2_H3K27ac_treat.bdg >  cropped_D2_H3K27ac_treat.bdg 
awk '{ if ($2 < 35507055 && $3 > 35502055) print $0}' D2_Sox2_R1/Scaled_NA_treat_pileup.bdg  > D2_Sox2_R1/cropped_NA_treat_pileup.bdg 
python Part1_plot.py D2_Sox2_R1/cropped_NA_treat_pileup.bdg cropped_D2_Klf4_treat.bdg cropped_D0_H3K27ac_treat.bdg cropped_D2_H3K27ac_treat.bdg’

#Part2
1&2.'sort -n -r -k 5 intersect_1.bed | head -300 > head_300_intersect_Sox2.bed'
3.'awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' head_300_intersect_Sox2.bed > reformatted_intersect_Sox2.sam'
4.'samtools faidx  mm10.fa -r reformatted_intersect_Sox2.sam > extracted_sequences.fasta'
5.'(meme) [~/qbb2022-answers/week5-homework $]conda activate meme
(meme) [~/qbb2022-answers/week5-homework $]meme-chip -maxw 7 extracted_sequences.fasta'
#Part 3
'(meme) [~/qbb2022-answers/week5-homework $]tomtom HOCOMOCOv11_full_MOUSE_mono_meme_format.meme memechip_out/combined.meme 
(meme) [~/qbb2022-answers/week5-homework $]grep -E 'KLF4|SOX2' tomtom_out/tomtom.tsv > tomtom_out/matches.txt'

