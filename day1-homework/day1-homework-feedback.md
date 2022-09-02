Really good work! 

For exercise 3:

This is an interesting way to covert spaces to tabs: `perl -p -i -e 's/ /\t/g' variants.bed`. It totally works, but I think that it might be easier to make this conversion by modify the existing awk command. `{OFS="\t"}` is an option that sets the Output Field Separator as tab. But both ways get you the right answer! 

– Andrew 
