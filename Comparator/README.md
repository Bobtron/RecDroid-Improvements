# Compares steps in bugreports about the same bug, against other steps in other bugreports about the same bug

First, download a pretrained word/phrase vector. I recommend google news vector here: https://code.google.com/archive/p/word2vec/
or Stanfords pre-trained word-vectors here: https://nlp.stanford.edu/projects/glove/

You can run the comparator via Driver.py like this:

python Driver.py path-to-model True/False-is-the-model-in-binary path-to-output-file

For example:

python Driver.py GoogleNews-vectors-negative300.bin True output.txt

You pass in the bug reports that are to have their steps compared via a hardcoded array inside of Driver.py
