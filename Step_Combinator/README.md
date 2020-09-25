# Combines stes after the Comparator
This Driver.py combines steps after running sets of bug reports throught the Comparator.

So what you have is something like this

0,0,1,0,0.539927
0,0,1,1,0.782518
...
3,4,4,3,0.866733

The similarity scores of each step to every other step. What this file will do is to crunch those numbers, and pair the steps that are most similar to each other, to create combined nodes.

Run Driver.py by passing in arguments.

python Driver.py path-to-Comparator-output

Then Driver.py should print out a list of merged nodes that can then be traversed.

Next step is the traversal
