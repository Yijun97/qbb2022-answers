# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 0.75 + 1 + 1 + 1 + 1 + 1 + 1 = 9.75 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * very good! --> +1

3. sort bam files and index sorted bam files (0.5 points each)

  * great! and cool use of the pipe for 3a. Interestingly enough, you can use just samtools sort and use the `-O bam` argument to specify you want a bam output --> +1

4. variant call with freebayes

  * want to use the `-p` argument to specify the ploidy of the yeast (1)
  * --> +0.75
  * I think freebayes should have been installed already?

5. filter variants

  * very good! --> +1
  * I think vcflib should have been installed already?

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * fantastic! --> +1

9. 4 panel plot (0.25 points each panel)

  * beautiful plot! --> +1

10. 1000 line vcf
