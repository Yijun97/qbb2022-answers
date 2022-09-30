This is a really good start, but there are definitely a few things that need to be addressed before this is "complete"

First and foremost, you shouldn't have two separate scripts for the AA and DNA alignments. Rather you want a single script that will run needleman-wunsch on whatever inputs you give it. So you should have one input each for 1) the input fasta, 2) the scoring matrix file, 3) the gap penalty, 4) the output file. Then your script should be able to run needleman-wunsch on whatever those inputs are. (-0.5)

I will also say that doing traceback by essentially redoing the F-matrix calculations is going to be slower, as you're essentially duplicating effort. Fill out the traceback matrix at the same time you're filling out the F-matrix, and then use the traceback matrix to do traceback (no points deducted)

When you are doing traceback, you either need to do `elif` to check if you did d, h, or v (or you need to add a `continue` statement to the end of each `if). As it stands right now, if there's a tie between any of these, you'll actually step backwards through the traceback matrix twice, and update the alignment twice. Additionally, your final alignment might be longer than either input sequence (so doing the max length of the two sequences doesn't work). Any gaps are going to increase the length of the assignment. Because of this, a `for` loop doesn't really make sense to do traceback. Rather you should be using a `while` loop to just check when you've gotten to the front of both sequences (-2.5)

7/10
