from nltk.parse.corenlp import CoreNLPParser
from nltk import Tree

parser = CoreNLPParser()
parse = next(parser.raw_parse("I put the book in the box on the table."))

# print(parse)

t = Tree.fromstring(str(parse))

t.pretty_print()