# QBB2022 - Day 1 - Homework Exercises Submission
Exercise 1: 
error messaage: awk: illegal field $(), name "nuc"
when I searched Google, I saw that "Use -v option in awk to pass shell variables to awk:", so I noticed that the variable "nuc"  was not delivered to akd properly. So I editted the exercise1.sh into:
awk -v nuc=$nuc '/^#/{next} {if ($4 == nuc) {print $5}}' $1 | sort | uniq -c
The readout: 
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
The output means, the highest percentage of mutation for base A is mutating to base G; for base C, the highest frequencey of mutation is  T; for base G, the highest frequency mutation  is A; for base T, the highest mutation is C.

Exercise2

According to the online source, the chromosome has 15 different states. We have to define which states are likely to be promoter. Active TSS, Flanking Active TSS, Bivalent/Poised TSS and Flanking Bivalent TSS/Enh, which are state 1,2,10 and 11. So for this file,  we have to find out all the regions marked with 1,2,10 or 11. 
(base) [~/qbb2022-answers/day1-homework $]awk '{if($4 == 1||$4 == 2||$4 == 10||$4 ==11){print}}' ~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed > promoter.bed
By the upper code, I saved all the chromatin regions with state 1/2/10/11 into promoter.bed
Then, I compared  promoter.bed with random_snippet.vcf and stored the result into intersect_out.bed
(base) [~/qbb2022-answers/day1-homework $]bedtools intersect -b promoter.bed -a ~/data/vcf_files/random_snippet.vcf > intersect_out.bed
At last, using exercise1.sh, I concluded the alternative mutation for each base.
(base) [~/qbb2022-answers/day1-homework $]bash exercise1.sh intersect_out.bed
Considering  A
   6 C
  32 G
   8 T
Considering  C
  12 A
  11 G
  39 T
Considering  G
  46 A
  17 C
  11 T
Considering  T
  10 A
  29 C
   8 G
T is the most alternate allele for C.

Exercise 3:
the first line produces a bed file which contains the chromosome name,  the exact position of each variant, and the biased position(-1) of each variant.
the second line is to make the file meet the requirements of bedtools/closest. It firstly sort the bed file by chromosome and  then by their start position.
after run the exercise3.sh, it showed that "Error: unable to open file or unable to determine types for file variants.bed"
this  error may resulted from some  unexpected spaces. 
perl -p -i -e 's/ /\t/g' variants.bed, removing spaces.
Then, it showed "Error: Sorted input specified, but the file variants.bed has the following out of order record"
so I sorted  the varianst.bed
sort -k1,1 -k2,2n variants.bed  > newvariants.bed
The exercise3.sh now  shows as:
awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
perl -p -i -e 's/ /\t/g' variants.bed # awk  -v OFS='/t/' {print $1,$2-1,$2} > variants.bed
sort -k1,1 -k2,2n variants.bed  > newvariants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a newvariants.bed -b genes.sorted.bed

Using awk '/^#/{next} {print $1,$2-1, $2}' $1 > variants.bed
perl -p -i -e 's/ /\t/g' variants.bed 
sort -k1,1 -k2,2n variants.bed  > newvariants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
Using `bash exercise3.sh ~/data/vcf_files/random_snippet.vcf | wc`
I found 10293 variants are returned;
Using `bash exercise3.sh ~/data/vcf_files/random_snippet.vcf |cut -f 7|sort|uniq|wc` 
I found there were 200 unique genes were returned.
so 10293/200 = 51.465 variants are connected to a gene on average.

