# Preprocess bug reports in order to turn sentences into bite sized steps

First, download stanford core nlp https://stanfordnlp.github.io/CoreNLP/

Then run

python Server.py

While Server.py is running, you can run

python Driver.py

And pass in bug reports, sentence by sentence, either via file input in command line, or simply hardcoded in Driver.py. This program should split the sentences into steps accordingly.
