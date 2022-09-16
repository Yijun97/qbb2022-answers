#Question 1. Coverage simulator

#Question 1.1. How many 100bp reads are needed to sequence a 1Mbp genome to 5x coverage? How many are needed for 15x coverage?
n = 1x10^6x5/100 = 50k; for 15x coverage, n = 1x10^6x15/100 = 150k

#Question 1.2. Write a program (in Python) to simulate sequencing 5x coverage of a 1Mbp genome with 100bp reads. The output of this simulation should be an array of length 1 million, where each element in the array is the coverage at that base.  Using this array, plot a histogram of the coverage. Then, overlay the histogram with a Poisson distribution with lambda=5.What do we need to do to transform these probabilities into a frequency count comparable to those in our histogram?
There are two ways for the  transformation.
1. We can use "density = True", to convert the y-axis into density(not the count)
2. We can set the poission probability "p" into p*1000000.
Using the density, the plot will look nicer, where the poisson has a better overlay visualization with the array. Thus I use the density instead of count number.

This was named with Exercise1.py.

#Question 1.3. Using your output array of coverages from Q1.2, how much of the genome (e.g., how many base pairs) has not been sequenced (has 0x coverage)? How well does this match Poisson expectations?
From my array, 6874 base pairs have 0x coverage. According to Poisson expectation, the number should be 6737.946999085467
I think this match is good.

#Question 1.4. Now repeat the analysis with 15x coverage: compute the number of bases with 0x coverage, and evaluate how well it matches the Poisson expectation.

27 base pairs have 0x coverage. According to Poisson expectation, the number should be 0.3059023205018258. This match is also good.

#Question 2. De novo assembly

#Using the data described in the Data section above, assemble the reads using Spades.
 After I ran this command: 'spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31'
 I got error saying "== Error ==  system call for: "['/Users/cmdb/miniconda3/bin/spades-hammer', '/Users/cmdb/qbb2022-answers/week1-homework/asm/asm/corrected/configs/config.info']" finished abnormally, OS return value: 22". I had no contigs.fasta.
 In the contigs.log file, I saw that this error was resulted from memory limit. After googling, I changed my command into 'spades.py --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm -t 4 -k 31 -m 1024', and finally got my contigs.fasta.

#2.1. How many contigs were produced? 
'grep -c '>' contigs.fasta', I got 4 contigs.

#2.2. What is the total length of the contigs?
[Hint: try samtools faidx, plus a short script if necessary]
'samtools faidx contigs.fasta'  -----get .fai file (contigs.fasta.fai)
'cat contigs.fasta.fai'  ----------get the content of fai.
NODE_1_length_105830_cov_20.649108	105830	36	60	61
NODE_2_length_47860_cov_20.367392	47860	107665	60	61
NODE_3_length_41351_cov_20.528098	41351	156358	60	61
NODE_4_length_39426_cov_20.336388	39426	198434	60	61

The columns are  explained as followed: 
1st,  NAME    Name of this reference sequence
2nd,  LENGTH  Total length of this reference sequence, in bases
3rd,  OFFSET  Offset within the FASTA file of this sequence's first base
4th,  LINEBASES   The number of bases on each line
5th,  LINEWIDTH   The number of bytes in each line, including the newline

So, the lengths for the 4 contigs are 105830, 47860, 41351, 39426， with a total length of 234467.
 

# 2.3. What is the size of your largest contig? 
'sort -k 2 -n contigs.fasta.fai'
NODE_4_length_39426_cov_20.336388	39426	198434	60	61
NODE_3_length_41351_cov_20.528098	41351	156358	60	61
NODE_2_length_47860_cov_20.367392	47860	107665	60	61
NODE_1_length_105830_cov_20.649108	105830	36	60	61
So, the largest contig has a size of 105830.

#2.4. What is the contig N50 size? 
(105830 + 47860 + 41351 + 39426)/2 = 117233.5, lies in NODE_2_length_47860_cov_20.367392. So N50 size is 47860bp.

#Question 3. Whole Genome Alignment
'[~/qbb2022-answers/week1-homework/asm/asm $]dnadiff ../ref.fa contigs.fasta'
The dnadiff was unable to run at first. It showed "bad interpreter: No such file or dictionary". So after googling, I tried  to reinstall perl.
'sudo ln -s /Users/cmdb/miniconda3/bin/perl /usr/local/bin/perl'
Thus, I could run 'dnadiff ../ref.fa contigs.fasta', and finally get the out.report.
But when I was about to run nucmer, I again met problems. It showed "ERROR: mummer or mgaps returned non-zero". Google told me this was resulted from the fact that the reference sequence is larger than is supported by default. I should change MUMmer3 into 64bits to increase  maximum reference permitted. But after I tried either "define SIXTYFOURBITS" before the line "#ifdef SIXTYFOURBITS" in MUMmer3.23/src/kurtz/libbasedir/typs.h and then run install to compile the package or "make clean" followed by "make CPPFLAGS="-O3 -DSITYFOURBITS"", the nucmer still didn't work. So I download MUMmer4 from “https://mummer4.github.io/manual/manual.html”. Later, I got the error bout illegal division by zero. So I changed all the 'x27' into '"'. In this way, I could further run nucmer. And I also updated my dnadiff readout.
#Question 3.1. What is the average identify of your assembly compared to the reference?
'[~/qbb2022-answers/week1-homework/asm/asm $]dnadiff ../ref.fa contigs.fasta'
According to the out.report, the average identity for 1-to-1 and M-to-M are both 99.9955. 
#Question 3.2. What is the length of the longest alignment 
'[~/qbb2022-answers/week1-homework/asm/asm $]nucmer ../ref.fa contigs.fasta 
[~/qbb2022-answers/week1-homework/asm/asm $]show-coords out.delta'
I got the following result:

    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
=====================================================================================
  127965   233794  |        1   105830  |   105830   105830  |    99.99  | Halomonas    NODE_1_length_105830_cov_20.649108
  226799   226897  |    93103    93201  |       99       99  |    96.97  | Halomonas    NODE_1_length_105830_cov_20.649108
   40651    88510  |        1    47860  |    47860    47860  |   100.00  | Halomonas    NODE_2_length_47860_cov_20.367392
       3    26789  |        1    26787  |    26787    26787  |   100.00  | Halomonas    NODE_3_length_41351_cov_20.528098
   26788    40641  |    27498    41351  |    13854    13854  |   100.00  | Halomonas    NODE_3_length_41351_cov_20.528098
   88532   127957  |        1    39426  |    39426    39426  |   100.00  | Halomonas    NODE_4_length_39426_cov_20.336388
the longest alignment has a length of 105830 bp.
#Question 3.3. How many insertions and deletions are in the assembly?
According to out.report, which is produced from Dnadiff, there are 712bp insertion in the assembly，and there are 51bp deletiion.

#Question 4. Decoding the insertion

#Question 4.1. What is the position of the insertion in your assembly? Provide the corresponding position in the reference. 

'show-coords out.delta'

    [S1]     [E1]  |     [S2]     [E2]  |  [LEN 1]  [LEN 2]  |  [% IDY]  | [TAGS]
=====================================================================================
  127965   233794  |        1   105830  |   105830   105830  |    99.99  | Halomonas    NODE_1_length_105830_cov_20.649108
  226799   226897  |    93103    93201  |       99       99  |    96.97  | Halomonas    NODE_1_length_105830_cov_20.649108
   40651    88510  |        1    47860  |    47860    47860  |   100.00  | Halomonas    NODE_2_length_47860_cov_20.367392
       3    26789  |        1    26787  |    26787    26787  |   100.00  | Halomonas    NODE_3_length_41351_cov_20.528098
   26788    40641  |    27498    41351  |    13854    13854  |   100.00  | Halomonas    NODE_3_length_41351_cov_20.528098
   88532   127957  |        1    39426  |    39426    39426  |   100.00  | Halomonas    NODE_4_length_39426_cov_20.336388
the position should be in the 'NODE_3_length_41351_cov_20.649108' contig, in position 26788 to 27497.

#Question 4.2. How long is the novel insertion? 
In NODE_3_length_41351_cov_20.528098, there are some sequences that are not matched with reference sequences. So I think this is the novel insertion. Length: 27497-26788+1=710bp

#Question 4.3. What is the DNA sequence of the encoded message? 
'[~/qbb2022-answers/week1-homework/asm/asm $]samtools faidx contigs.fasta NODE_3_length_41351_cov_20.528098:26788-27497'
I got this:
>NODE_3_length_41351_cov_20.528098:26788-27497
ATACAATGCGTATTGTAGTATGGCCTTACGGGAGGGCAGACGGCAAAGAGTGATCACGTT
CTATCGGATGCAAGGCACCGCTTTATCCATTAGCCTCTTATTGGAGGAGGGCATGGCATT
CATACCCAATGGCTCAATTCTTTTACTACAACATTGATAACTTATCCAAGTACTCTACGA
CCAACCTGCAGAACGGCCCACCGGCCTAACGGCATACCTCACAACTACCCTGCTAAGGCG
AGCACTCCAGCCAAGCAAGACCACATCCACCCAAGCCCACCTCATCGCCTCAGCCAATAG
CGCTCAGACAAAAGGAACTTATTATTAACTGAAACGCTGTACTGCGGTAAGTCCTCAACG
CCGACCAAACGAAACCAGCAGCGTAGTCCTATCGGACTCGCTTGCACACATAACACATGC
TTGTAGTCTTGCACGACCCCAGGCGGACATGAGTTTCTGCTGGGCGGCGAGGAGTCGAAG
CTGCGGGCATTCCTTTCCGAAAACATGAATTACTGCGGGTATGTCCGACCTCAAACATTC
GTACCTGAGCATATTGCTCAAGTGAGCCAGTCGGCAATTCATATCCGAAAACATGACTGT
CTTGCATAAGGCCTCTCTTACGAGCTGAGTGCACGAACCACGGAACAGCTTAGTCACTTA
GAAGAGTACTCTATTCGGGACTTGAAGTACGCGTGCAATCGGGAACTAGT

This is the insertion sequence.

#Question 4.4. What is the secret message?
'[~/qbb2022-answers/week1-homework/asm/asm $]samtools faidx contigs.fasta NODE_3_length_41351_cov_20.528098:26788-27497 > extract.fa
[~/qbb2022-answers/week1-homework/asm $]python dna-decode.py --decode --input asm/extract.fa '
I got the message, finally!!!
The decoded message :  Congratulations to the 2022 CMDB @ JHU class!  Keep on looking for little green aliens..

