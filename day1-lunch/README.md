# QBB2022  - Day  1 - Lunch Exercises Submission

Question 2:
Code:
(base) [~ $]ls
Desktop		Movies		Sites		data		qbb2022-answers
Documents	Music		bin		day1-morning	tmp.txt
Downloads	Pictures	cmdb-quantbio	init
Library		Public		code		miniconda3
(base) [~ $]cd qbb2022-answers/
(base) [~/qbb2022-answers $]mkdir day1-lunch .
mkdir: .: File exists
(base) [~/qbb2022-answers $]ls
README.md	day1-lunch
(base) [~/data $]cp bed_files/genes.chr21.bed ../qbb2022-answers/day1-lunch/
(base) [~/data $]cp bed_files/exons.chr21.bed ../qbb2022-answers/day1-lunch/
(base) [~/data $]cd ../qbb2022-answers/day1-lunch/
(base) [~/qbb2022-answers/day1-lunch $]ls
README.md	exons.chr21.bed	genes.chr21.bed
(base) [~/qbb2022-answers/day1-lunch $]cd exons.chr21.bed 
README.md        exons.chr21.bed  genes.chr21.bed  
(base) [~/qbb2022-answers/day1-lunch $]wc exons.chr21.bed 
   13653   40959  327672 exons.chr21.bed
(base) [~/qbb2022-answers/day1-lunch $]wc genes.chr21.bed 
     219     657    5256 genes.chr21.bed

Answer:
mean number of exons per gene = 13653/219 = 62.34

To find the median :
1. match the exons to each gene by corresponding start position and end position;
2. calculate each gene's exon number;
3. sort each gene's exon number;
4. count the number of genes;
5. find the median number of genes, which is short for x;
6. find the exon number in "x" position, and this is the median exon number.

Question 3:

Code:
(base) [~/data/bed_files $]cp chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed ../../qbb2022-answers/day1-lunch/
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | sort | uniq
1
10
11
12
13
14
15
2
3
4
5
6
7
8
9
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 1 | wc
     305     305     610
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 10 | wc
      17      17      51
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 11 | wc
      17      17      51
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 12 | wc
      30      30      90
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 13 | wc
      62      62     186
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 14 | wc
     228     228     684
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 15 | wc
     992     992    2976
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 2 | wc
     678     678    1356
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 3 | wc
      79      79     158
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 4 | wc
     377     377     754
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 5 | wc
     808     808    1616
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 6 | wc
     148     148     296
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 7 | wc
    1050    1050    2100
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 8 | wc
     156     156     312
(base) [~/data/bed_files $]cut -f 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | grep -w 9 | wc
     654     654    1308

Answer:
For state 1, there are 305 regions;
For state 2, there are 678 regions;
For state 3, there are 79 regions;
For state 4, there are 377 regions;
For state 5, there are 808 regions;
For state 6, there are 148 regions;
For state 7, there are 1050 regions;
For state 8, there are 156 regions;
For state 9, there are 654 regions;
For state 10, there are 17 regions;
For state 11, there are 17 regions;
For state 12, there are 30 regions;
For state 13, there are 62 regions;
For state 14, there are 228 regions;
For state 15, there are 992 regions;

state for 3-2 get basic range, add to a total..largest one

Question 4:
(base) [~/data/metadata_and_txt_files $]cp integrated_call_samples.panel ../../qbb2022-answers/day1-lunch/
(base) [~/data/metadata_and_txt_files $]cut -f 2,3 integrated_call_samples.panel | grep AFR | cut -f 1 | sort | uniq -c	
 123 ACB
 112 ASW
 173 ESN
 180 GWD
 122 LWK
 128 MSL
 206 YRI
 
Answer:
There are 123 samples in ACB subpopulations;
There are 112 samples in ASW subpopulations;
There are 173 samples in ESN subpopulations;
There are 180 samples in GWD subpopulations;
There are 122 samples in LWK subpopulations;
There are 128 samples in MSL subpopulations;
There are 206 samples in YRI subpopulations;

As for all five populations, 
1. use 
(base) [~/data/metadata_and_txt_files $]cut -f 3 integrated_call_samples.panel |sort | uniq
AFR
AMR
EAS
EUR
SAS
to get the name of the five populations.
2. I may just apply the same code:
(base) [~/data/metadata_and_txt_files $]cut -f 2,3 integrated_call_samples.panel | grep xxx | cut -f 1 | sort | uniq -c	
xxx stands for each name of the five populations.

Question 5:
(base) [~/data/vcf_files $]cp random_snippet.vcf ../../qbb2022-answers/day1-lunch/
(base) [~/qbb2022-answers/day1-lunch $]cut -f 1,2,3,4,5,6,7,8,9,13 random_snippet.vcf > HG00100.vcf
(base) [~/qbb2022-answers/day1-lunch $]cut -f 10 HG00100.vcf | sort | uniq -c
   1 ##FILTER=<ID=PASS,Description="All filters passed">
   1 ##FORMAT=<ID=GT,Number=1,Type=String,Description="Phased Genotype">
   1 ##INFO=<ID=AC,Number=A,Type=Integer,Description="Total number of alternate alleles in called genotypes">
   1 ##INFO=<ID=AF,Number=A,Type=Float,Description="Estimated allele frequency in the range (0,1)">
   1 ##INFO=<ID=AFR_AF,Number=A,Type=Float,Description="Allele frequency in the AFR populations calculated from AC and AN, in the range (0,1)">
   1 ##INFO=<ID=AMR_AF,Number=A,Type=Float,Description="Allele frequency in the AMR populations calculated from AC and AN, in the range (0,1)">
   1 ##INFO=<ID=AN,Number=1,Type=Integer,Description="Total number of alleles in called genotypes">
   1 ##INFO=<ID=DP,Number=1,Type=Integer,Description="Approximate read depth; some reads may have been filtered">
   1 ##INFO=<ID=EAS_AF,Number=A,Type=Float,Description="Allele frequency in the EAS populations calculated from AC and AN, in the range (0,1)">
   1 ##INFO=<ID=EUR_AF,Number=A,Type=Float,Description="Allele frequency in the EUR populations calculated from AC and AN, in the range (0,1)">
   1 ##INFO=<ID=EX_TARGET,Number=0,Type=Flag,Description="indicates whether a variant is within the exon pull down target boundaries">
   1 ##INFO=<ID=NS,Number=1,Type=Integer,Description="Number of samples with data">
   1 ##INFO=<ID=SAS_AF,Number=A,Type=Float,Description="Allele frequency in the SAS populations calculated from AC and AN, in the range (0,1)">
   1 ##INFO=<ID=VT,Number=.,Type=String,Description="indicates what type of variant the line represents">
   1 ##contig=<ID=chr21>
   1 ##fileDate=31052018_15h52m43s
   1 ##fileformat=VCFv4.3
   1 ##reference=ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa
   1 ##source=IGSRpipeline
9514 0|0
 127 0|1
 178 1|0
 181 1|1
   1 HG00100
(base) [~/qbb2022-answers/day1-lunch $]grep -w "AF=1" HG00100.vcf |wc
      15     150    1884

Answer:
c. 9514 for 0|0, 127 for 0|1, 178 for 1|0, 181 for 1|1
d. 15
e. 1
f. (base) [~/qbb2022-answers/day1-lunch $]grep -v "#" HG00100.vcf | cut -f 8 | cut -d ";" -f 7
we use "cut -f 8" to find  out the columns that contain AFR, and then use "cut -d "," -f 7" to extract AFR values, for every line contains AFR.
