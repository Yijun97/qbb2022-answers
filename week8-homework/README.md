(base) [~/qbb2022-answers/week8-homework $]conda create -n medaka medaka
(base) [~/qbb2022-answers/week8-homework $]pip install whatshap==1.
(base) [~/qbb2022-answers/week8-homework $]curl https://bx.bio.jhu.edu/data/msauria/cmdb-lab/ont_data.tar.gz --output ont_data.tar.gz
(base) [~/qbb2022-answers/week8-homework $]tar xzf ont_data.tar.gz
(base) [~/qbb2022-answers/week8-homework $]conda activate medaka
(medaka) [~/qbb2022-answers/week8-homework $]medaka_variant -h
(medaka) [~/qbb2022-answers/week8-homework $]medaka_variant -i methylation.bam  -f hg38.fa -r "chr11:1900000-2800000" -o chr11 -p chr11.vcf
(medaka) [~/qbb2022-answers/week8-homework $]medaka_variant -i methylation.bam  -f hg38.fa -r "chr14:100700000-100990000" -o chr14  -p chr14.vcf
(medaka) [~/qbb2022-answers/week8-homework $]medaka_variant -i methylation.bam  -f hg38.fa -r "chr15:23600000-25900000" -o chr15  -p chr15.vcf
(medaka) [~/qbb2022-answers/week8-homework $]medaka_variant -i methylation.bam  -f hg38.fa -r "chr20:58800000-58912000" -o chr20  -p chr20.vc
(medaka) [~/qbb2022-answers/week8-homework $]whatshap haplotag -o chr11/haplotagged_chr11.bam -r chr11:1900000:2800000 --reference hg38.fa chr11/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr11/Haplotag_chr11
== SUMMARY ==
Total alignments processed:                     16545
Alignments that could be tagged:                 3323
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 11.728080034255981
(medaka) [~/qbb2022-answers/week8-homework $]whatshap haplotag -o chr14/haplotagged_chr14.bam -r chr14:100700000:100990000 --reference hg38.fa chr14/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr14/Haplotag_chr14
== SUMMARY ==
Total alignments processed:                     16545
Alignments that could be tagged:                 1303
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 10.365786075592041
(medaka) [~/qbb2022-answers/week8-homework $]whatshap haplotag -o chr15/haplotagged_chr15.bam -r chr15:23600000:25900000 --reference hg38.fa chr15/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr15/Haplotag_chr15
== SUMMARY ==
Total alignments processed:                     16545
Alignments that could be tagged:                 8000
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 14.05019998550415
(medaka) [~/qbb2022-answers/week8-homework $]whatshap haplotag -o chr20/haplotagged_chr20.bam -r chr20:58800000:58912000 --reference hg38.fa chr20/round_0_hap_mixed_phased.vcf.gz methylation.bam --output-haplotag-list chr20/Haplotag_chr20
== SUMMARY ==
Total alignments processed:                     16545
Alignments that could be tagged:                   87
Alignments spanning multiple phase sets:            0
haplotag - total processing time: 9.910881996154785

(medaka) [~/qbb2022-answers/week8-homework $]whatshap split --output-h1 chr11/h1.bam --output-h2 chr11/h2.bam chr11/haplotagged_chr11.bam chr11/haplotag_chr11
== SUMMARY ==
Total reads processed: 16545
Number of output reads "untagged": 0
Number of output reads haplotype 1: 1625
Number of output reads haplotype 2: 1698
Number of unknown (dropped) reads: 0
Number of skipped reads (per user request): 13222
Time for processing haplotag list: 0.01 sec
Time for total initial setup: 0.012 sec
Time for iterating input reads: 3.501 sec
Total run time: 3.516 sec

(medaka) [~/qbb2022-answers/week8-homework $]whatshap split --output-h1 chr14/h1.bam --output-h2 chr14/h2.bam chr14/haplotagged_chr14.bam chr14/haplotag_chr14
== SUMMARY ==
Total reads processed: 16545
Number of output reads "untagged": 0
Number of output reads haplotype 1: 638
Number of output reads haplotype 2: 665
Number of unknown (dropped) reads: 0
Number of skipped reads (per user request): 15242
Time for processing haplotag list: 0.01 sec
Time for total initial setup: 0.012 sec
Time for iterating input reads: 2.385 sec
Total run time: 2.401 sec

(medaka) [~/qbb2022-answers/week8-homework $]whatshap split --output-h1 chr15/h1.bam --output-h2 chr15/h2.bam chr15/haplotagged_chr15.bam chr15/haplotag_chr15
== SUMMARY ==
Total reads processed: 16545
Number of output reads "untagged": 0
Number of output reads haplotype 1: 3996
Number of output reads haplotype 2: 4004
Number of unknown (dropped) reads: 0
Number of skipped reads (per user request): 8545
Time for processing haplotag list: 0.011 sec
Time for total initial setup: 0.013 sec
Time for iterating input reads: 5.972 sec
Total run time: 5.991 sec

(medaka) [~/qbb2022-answers/week8-homework $]whatshap split --output-h1 chr20/h1.bam --output-h2 chr20/h2.bam chr20/haplotagged_chr20.bam chr20/haplotag_chr20
== SUMMARY ==
Total reads processed: 16545
Number of output reads "untagged": 0
Number of output reads haplotype 1: 43
Number of output reads haplotype 2: 44
Number of unknown (dropped) reads: 0
Number of skipped reads (per user request): 16458
Time for processing haplotag list: 0.01 sec
Time for total initial setup: 0.012 sec
Time for iterating input reads: 1.731 sec
Total run time: 1.746 sec
(Medaka) [~/qbb2022-answers/week8-homework $]samtools cat -o H1.bam chr11/h1.bam chr14/h1.bam chr15/h1.bam chr20/h1.bam
(Medaka) [~/qbb2022-answers/week8-homework $]samtools cat -o H2.bam chr11/h2.bam chr14/h2.bam chr15/h2.bam chr20/h2.bam
(Medaka) [~/qbb2022-answers/week8-homework $]samtools index H1.bam 
(Medaka) [~/qbb2022-answers/week8-homework $]samtools index H2.bam 
(medaka) [~/qbb2022-answers/week8-homework $]conda deactivate
(base) [~/qbb2022-answers/week8-homework $]conda create -n igv gradle openjdk=11 -y
(base) [~/qbb2022-answers/week8-homework $]conda activate igv
(igv) [~/qbb2022-answers/week8-homework $]git clone https://github.com/igvteam/igv.git
(igv) [~/qbb2022-answers/week8-homework $]cd igv
(igv) [~/qbb2022-answers/week8-homework/igv $]./gradlew createDist
(igv) [~/qbb2022-answers/week8-homework/igv $]cd ../
(igv) [~/qbb2022-answers/week8-homework $]ln -s ${PWD}/igvbuild/IGV-dist/igv.sh ./


#6 Do you expect each region in H1 or H2 to correspond to the same parent of origin (i.e. the same haplotype)? Explain your reasoning.
Yes, each region in H1 or H2 will correspond to the same parent. For when we run the whatshap haplotag subcommand on the phased VCF file, it tags each read in a BAM file with H1 or H2 depending on which haplotype it belongs to, and also adds a PS tag that describes in which haplotype block the read is. thus, the H1 and H2 is not randomly assigned, but is determined. So the regions in H1 or H2 has the same origion.

