#Quantitative Biology week3 homework
#Step 1:
'bwa index sacCer3'
get the sacCer3.fa file

#Step2 :
'bash Step2_loop.bash' 

#Step3a:
'bash Step3a_loop.bash'
transfer the sam files produced in step2 into sorted bam files

#Step3b:
'bash Step3b_loop.bash'
index the sorted bam files

#Step 4
'git clone --recursive https://github.com/freebayes/freebayes.git'
to install freebayes
'freebayes -f sacCer3.fa --genotype-qualities *.bam > output.vcf'
create the vcf for all the 10 yeast strains.

#Step5
'conda install -c bioconda vcflib'
install vcflib
'vcffilter -f "QUAL > 20" output.vcf > filtered_output.vcf'
create the filtered vcf after filtering out the variants whose estimated probability of being polymorphoric is less than or equal to0.99

#Step6 
'vcfallelicprimitives -k -g filtered_output.vcf > decomposed_output.vcf'
create vcf containing information about decomposed complex haplotypes

#Step7
'conda install snpeff=5.0 -y'
'snpeff download R64-1-1.99'
'snpeff ann R64-1-1.99 decomposed_output.vcf > annotated_output.vcf'

#Step8
'python Step8_plot.py annotated_output.vcf'

#create the first 1000 lines of annotated vcf
head -n 10000 annotated_output.vcf  > head_annotated_output.vcf