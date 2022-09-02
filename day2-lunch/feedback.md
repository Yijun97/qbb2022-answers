# Feedback day2-lunch

Overall, this is a good start. You demonstrate a basic comfort with this level of python and understand the logic to writing the various checks. You just didn't go quite far enough.

- You are only converting RGB if fieldN is exactly 9.
- You are only checking fields[10] and fields[11] if fieldN is exactly 12, but you have no check to make sure it isn't larger.
- You are not modifying or overwriting the original fields when you process fields 8, 10, and 11 so any changes you make are lost.
- For fields 8, 10, and 11, each item after they are split should be changed into an int
- when you find a bad field, you add to the count, but continue processing the line. This means that the same line can increment count multiple times. Also, it still gets included in the bed list. You could use the `continue` statement to end the current loop iteration and move on to the next one each time you have a `count = count + 1` statement.

 One of the biggest challenges people have when learning lists is understanding when the variables inside the list get changed and when they don't. It is safe practice to assume that if you don't have a statement like `fields[i] =`, `fields[i]` is not going to be updated no matter what you do with the value you copied out of it. You're making good progress. Keep it up!