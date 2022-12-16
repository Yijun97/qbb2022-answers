This is a really good start, but there are definitely a few things that need to be addressed before this is "complete"

First and foremost, you shouldn't have two separate scripts for the AA and DNA alignments. Rather you want a single script that will run needleman-wunsch on whatever inputs you give it. So you should have one input each for 1) the input fasta, 2) the scoring matrix file, 3) the gap penalty, 4) the output file. Then your script should be able to run needleman-wunsch on whatever those inputs are. (-0.5)

I will also say that doing traceback by essentially redoing the F-matrix calculations is going to be slower, as you're essentially duplicating effort. Fill out the traceback matrix at the same time you're filling out the F-matrix, and then use the traceback matrix to do traceback (no points deducted)

When you are doing traceback, you either need to do `elif` to check if you did d, h, or v (or you need to add a `continue` statement to the end of each `if). As it stands right now, if there's a tie between any of these, you'll actually step backwards through the traceback matrix twice, and update the alignment twice. Additionally, your final alignment might be longer than either input sequence (so doing the max length of the two sequences doesn't work). Any gaps are going to increase the length of the assignment. Because of this, a `for` loop doesn't really make sense to do traceback. Rather you should be using a `while` loop to just check when you've gotten to the front of both sequences (-2.5)

7/10

REGRADE 12/16/2022 -- Dylan

This is a solid re-work. Good work incorporating `sys.argv` to handle inputs from the command line, and for using a `while` loop during traceback. That said, some of the other things I pointed out are still incorrect:
1. The way you're doing traceback--filling out the F-matrix, and then going backwards and re-determining which direction you chose--is slow. You shouldn't be recalculating d, h, and v during traceback and filling out the traceback matrix then. Rather, as you're moving forward filling out the F matrix, just also fill out the traceback matrix with whatever direction you chose at the time. As you have it now, you're not actually even using the traceback matrix. This isn't a huge deal by any means, and it only doubles the compute time (which in the grand scheme of things, isn't too bad), but it is the type of thing you want to think about in the future. (no points deducted)
2. You still need to use `elif` or continue statements when checking d,h, or v for traceback. It's not a huuuuge issue, because you're updating indicies and the final alignments correctly, BUT you can accidently step past the beginning of the sequences if you have d, h, and v alignments in a row, because it will run each of the corresponding code blocks before the while loop sees that you're at the beginning of the sequences. And actually, I think that's happening in your DNA alignment. ALSO, when you're updating your indicies, you need to do that AFTER you append the correct characters to the alignments, because otherwise you'll be appending the character before the correct character. (-0.25)

Overall, great work though!

(9.75/10)
