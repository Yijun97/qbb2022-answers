Step 1A
'(base) [~/qbb2022-answers/week13-homework $]git clone https://github.com/marbl/Krona.git
(base) [~/qbb2022-answers/week13-homework $]cd Krona/KronaTools/
(base) [~/qbb2022-answers/week13-homework $]sudo ./install.pl'

Step 1B
'(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492183.kraken SRR492183
(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492186.kraken SRR492186
(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492188.kraken SRR492188
(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492189.kraken SRR492189
(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492190.kraken SRR492190
(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492193.kraken SRR492193
(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492194.kraken SRR492194
(base) [~/qbb2022-answers/week13-homework $]python parseKRAKEN.py ~/cmdb-quantbio/metagenomics_data/step0_givendata/KRAKEN/SRR492197.kraken SRR492197
Step 1C
(base) [~/qbb2022-answers/week13-homework $]ktImportText -q *_krona.txt '

#Question 1: briefly comment on the trends you see in the gut microbiota throughout the first week.
The portion of Viruse is decreasing; the portion of tenterococcus faecalls increases at first, and then falls down. The alpha diverisity decreases and then increases.

Step2 deconvolute the assembled scaffolds into individual genomes(binning)
align the reads from multiple samples to the assembly to get the coverage of each contig in all the samples. 
#Question 2: comment on what metrics in the contigs could we use to group them together?
They have end sequences overlapping, thus we could group them together.

step 2A
'(base) [~/qbb2022-answers/week13-homework $]bwa index ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta 
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492183_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492183_2.fastq > SRR492183.sam
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492186_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492186_2.fastq > SRR492186.sam
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492188_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492188_2.fastq > SRR492188.sam
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492189_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492189_2.fastq > SRR492189.sam
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492190_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492190_2.fastq > SRR492190.sam
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492193_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492193_2.fastq > SRR492193.sam
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492194_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492194_2.fastq > SRR492194.sam
bwa mem -t 4 ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492197_1.fastq ../../cmdb-quantbio/metagenomics_data/step0_givendata/READS/SRR492197_2.fastq > SRR492197.sam'

Step2B
'(base) [~/qbb2022-answers/week13-homework $]samtools sort SRR492186.sam -o SRR492186.bam
(base) [~/qbb2022-answers/week13-homework $]samtools sort SRR492188.sam -o SRR492188.bam
(base) [~/qbb2022-answers/week13-homework $]samtools sort SRR492189.sam -o SRR492189.bam
(base) [~/qbb2022-answers/week13-homework $]samtools sort SRR492190.sam -o SRR492190.bam
(base) [~/qbb2022-answers/week13-homework $]samtools sort SRR492193.sam -o SRR492193.bam
(base) [~/qbb2022-answers/week13-homework $]samtools sort SRR492194.sam -o SRR492194.bam
(base) [~/qbb2022-answers/week13-homework $]samtools sort SRR492197.sam -o SRR492197.bam'

Step2C Repair the metaBAT2 environment

'(metabat2) [~/qbb2022-answers/week13-homework $]metabat2 -i ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta -a depth.txt -o bins_dir/bin'
MetaBAT 2 (2.15 (Bioconda)) using minContig 2500, minCV 1.0, minCVSum 1.0, maxP 95%, minS 60, maxEdges 200 and minClsSize 200000. with random seed=1670617045
6 bins (13187322 bases in total) formed.
#Question 3A
I got 6 bins.
#Question 3B:
'(metabat2) [~/qbb2022-answers/week13-homework $]grep ">" ../../cmdb-quantbio/metagenomics_data/step0_givendata/assembly.fasta| awk -F'_' '{SUM+=$4; print $4} END {print "total length is:"SUM}''
total length is:38071686
'(metabat2) [~/qbb2022-answers/week13-homework $]for FA in bins_dir/*.fa; do echo $FA;grep ">" $FA| awk -F'_' '{SUM+=$4;} END {print "total length is:"SUM}'; done'
(bin 1)total length is:2705023, representing 7.1% of the total assembly
(bin 2)total length is:2251850, representing 5.9% of the total assembly
(bin 3)total length is:1656034, representing 4.3% of the total assembly
(bin 4)total length is:1227903, representing 3.2% of the total assembly
(bin 5)total length is:2483660, representing 6.5% of the total assembly
(bin 6)total length is:2862852, representing 7.5% of the total assembly
#Question 3C:
These 6 bins only have less than 3Mb genome size. For prokaryotic genome, the common size is around 5Mb. Thus, these sizese don't seem to be right.
#Question 3D:

Step 3
I wrote a unix script to do this.
(metabat2) [~/qbb2022-answers/week13-homework/bins_dir $]bash Taxonomic_composition_prediction.sh 
And I got six files containing the taxinomic prediction results.
#Question 4
(A)
Bin 1: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus aureus;Staphylococcus aureus subsp. aureus;Staphylococcus aureus subsp. aureus ST72;Staphylococcus aureus subsp. aureus CN1
Bin 2: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus epidermidis;Staphylococcus epidermidis RP62A
Bin 3: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Tissierellia;Tissierellales;Peptoniphilaceae;Anaerococcus;Anaerococcus prevotii;Anaerococcus prevotii DSM 20548
Bin 4: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Bacillales;Staphylococcaceae;Staphylococcus;Staphylococcus haemolyticus;Staphylococcus haemolyticus JCSC1435
Bin 5: root;cellular organisms;Bacteria;Terrabacteria group;Actinobacteria;Actinobacteria;Propionibacteriales;Propionibacteriaceae;Cutibacterium;Cutibacterium avidum;Cutibacterium avidum 44067
Bin 6: root;cellular organisms;Bacteria;Terrabacteria group;Firmicutes;Bacilli;Lactobacillales;Enterococcaceae;Enterococcus;Enterococcus faecalis;Enterococcus faecalis OG1RF or V583
(B)
We can reducing memory usage of Kraken, to allow greater amounts of reference genomic data to be used and maintain high accuracy and increase speed fivefold.