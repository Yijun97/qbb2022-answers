# QBB2022 - Day 4 - lunch Exercises Submission

#Exercise 1: Reproduce plots using bxlab/cmdb-plot-vcfs

i. Portion of do_all.sh output (not script) that reports how many bp each feature covers：
"protein_coding.chr21" covers 13780687 bp
"processed_pseudogene.chr21" covers 956640 bp
"exons.chr21" covers 1107407 bp

ii. One or more strategies to confirm that reproduced plots are the same as in the cache/ directory
The first method:use "open filename" to open the reproduced plots from bash, and compare them with the plots in the cache/ directory
The second method: check the base number
cmp -b <file1> < file2> there is some differences resulted from matplotlib version
diff is another function that could be used (diff -md6sum)



iii. Three other gene_types present in the GENCODE .gtf that you find interesting and why
the first one: retained intron. The introns usually aren't transcripted, and it is likely that there are little similarity between different introns in different people. But these regions, marked as retained intron, indicate their possible roles in gene regulation. They may be important for effective gene transcription as regulatory elements or be import mutation sites.
the second one: non-sense mediated decay. There are non-sense mediated dacay events happen in most cells. This process may be important to keep the genome integrate. It is also possible for these regions to play a role in cell apoptosis.
the third one: lncRNA. these long RNAs may be a regulator in epigenetic regulation. For example, Xist, which is a long RNA present in X chromosome, is crucial to keep one of the X chromosomes silent in female. So it is interesting to investigate other lncRNA.

#2. Modify workflow

Modified：

‘fig, ax = plt.subplots()
ax.hist( ac, density=True )
ax.set_yscale("log")
ax.set_ylim(1e-8, 1e-2)
ax.set_title(vcf)
ax.set_xlabel("AC counts")
ax.set_ylabel("Frequency")
fig.savefig( vcf + ".png" )
plt.show()
fs.close()’
To deal with AC data that includes zero, we set a y limit, to avoid log(0).

Describe possible trends among plots in README.md

Exons and processed_pseudogene regions are less likely to have higher AC counts, while lncRNA and pretein-coding regions are relatively evenly distributed along the AC counts axis, meaning they have no preference for AC counts. That is likely resulted from the fact that exons and genes tend to have less mutations to maintain a normal protein. Too much mutations may result in eliminativ traits and make this allele no longer able to be transferred to the next generation.


#3. Create documentation
Add documentation for bxlab/cmdb-plot-vcfs in day4-lunch/README.md including:

Synopsis – <50 words
This folder contains the bash script and two files to generate gene_types of interests to produce bed files and vcf files, and also python scripts to produce the plot of each interested gene_type regarding the alleles number and their frequency for each sample. 

Usage – syntax including input file requirements
bash do_all.sh <thing1> <thing2>

Dependencies – software requirements
bedtools, matplotlib

Description – how it works (bullet points or prose)
1. Create .bed files for features of interst
-run the bash script "subset_region_bash", which contains gene regions of interest, and generate .bed files for feaatures of interest. you can set your feature of interest in the subse_regiion_bash.
2. Use bedtools -- intersect  to generate .vcf files from .bed files.
3. run the python to get the plot for each feaature of interest. the x axis stands for the number of AC, and the y axis stands for the frequency of  each AC number.

Output – example output
the plot regarding the AC counts and their frequency.

















