# Week 1 Genome Assembly -- Feedback

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10 points out of 10 possible points

1. Question 1.1, 1.4 how many reads (0.5 pts each)

  * good --> +1

2. Question 1.2, 1.4 simulation script(s)

  * very good --> +1
  * consider having one script for the simulation and plotting where you change the number of reads that are simulated, etc. using `sys.argv`

3. Question 1.2, 1.4 plotting script(s)

  * In addition to using `density = True` within the `hist` function, you could fit/overlay specifically a poisson curve. You could use the scipy `stats.poisson.pmf` function that you use later, together with `plt.plot` to accomplish this. That way you're fitting a specific Poisson function with a known `mu` or `lambda`. But you are correct that the `density=True` argument does turn the frequency counts into probabilities analogous to what `stats.poisson.pmf` returns.
  * --> +1

4. Question 1.2, 1.4 histograms with overlaid Poisson distributions (0.5 pts each)

  * Consider changing the plot titles in order to distinguish the 5x from the 15x coverage
  * good work overall --> +1

5. Question 1.3, 1.4 how much of genome not sequenced/comparison to Poisson expectations (0.5 pts each, 0.25 for answer and 0.25 for code)

  * good --> +1

6. Question 2 De novo assembly (0.5 pts each, 0.25 for answer and 0.25 for code)

  * number of contigs --> +0.5
  * total length of contigs --> +0.5

7. Question 2 De novo assembly cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * size of largest contig --> +0.5
  * contig n50 size --> +0.5

8. whole genome alignment (0.33 pts each, 0.33/2 for answer and 0.33/2 for code)

  * average identity --> +0.33
  * length of longest alignment --> +0.33
  * how many insertions and deletions in assembly --> +0.33

9. decoding the insertion (0.5 pts each, 0.25 for answer and 0.25 for code)

  * position of insertion in assembly --> +0.5
  * length of novel insertion --> +0.5

10. decoding the insertion cont (0.5 pts each, 0.25 for answer and 0.25 for code)

  * DNA sequence of encoded message --> +0.5
  * secret message --> +0.5

Fantastic work and great job recording what you did and how you interpreted results!
