## Week 6 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 13 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  

4. Script set up to log transform the scores

5. Script set up to shift the data by subtracting minimum value

6. Script set up to convert sparse data into square matrix

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?
  * highlighted signal indicates?

You don't need `for` loops for all of these steps in your code. You can take the log, fill the square matrix, find and subtract the minimum... all without the for loop. What you have works, but you can do it with single lines of code that will apply the operation to the whole data array at the same time, much like how you subtract the minimum score from the whole matrix. Please let me know if you have questions on this or want to see some examples.

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target; --> your `upscore` variable looks up and down, and so you don't need your `downscore` variable and the average you take of `upscore` and `downscore`.

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)
