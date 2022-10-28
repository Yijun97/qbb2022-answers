#QBB week6 homework
Take a look at the HiCContactRanges and HiCFragment plots 
What percentage of reads are valid interactions (duplicates do not count as valid)?
What constitutes the majority of invalid 3C pairs? What does it actually mean (you may need to dig into the HiC-Pro manual)?
1. dCTCF
37.8% * 92% = 34.78% of reads are valid interactions. 
the majority of invalid 3C pairs are Danging_end_pairs. Danging end means unligated fragments(boith reads mapped to the same restriction fragment).

2. ddCTCf
36.6% * 88% = 32.21% of reads are valid interactions. 
the majority of invalid 3C pairs are Danging_end_pairs.Danging end means unligated fragments(boith reads mapped to the same restriction fragment).
#Part2 Exploring the results by plotting heatmaps
'python load_data.py analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed dCTCF'
start_bin = 343067, and this correlates to "chr15	11168000	11174400	343067", one of the ends is out of the desired bin range.
end_bin = 343208,and this correlates to "chr15	12070400	12076800	343208", one of the ends is out of the desired bin range.

(base) [~/qbb2022-answers/week6-homework $]python week6.py analysis/hic_results/matrix/ddCTCF/iced/6400/ddCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/iced/6400/dCTCF_ontarget_6400_iced.matrix analysis/hic_results/matrix/dCTCF/raw/6400/dCTCF_ontarget_6400_abs.bed iced_data
(base) [~/qbb2022-answers/week6-homework $]python week6.py matrix/ddCTCF_full.6400.matrix matrix/dCTCF_full.6400.matrix matrix/6400_bins.bed full_data

1. Were you able to see the highlighted difference from the original figure?
It is hard to see the highlighted difference from the origianl figure.

2. What impact did sequencing depth have?
With higher sequencing length, the highlighted differences seem to be more obvious.

3. What does the highlighted signal indicate?
The difference between the interaction of this two genes with other regions.

for insulator plot:
(base) [~/qbb2022-answers/week6-homework $]python Insulator.py matrix/dCTCF_full.40000.matrix 

