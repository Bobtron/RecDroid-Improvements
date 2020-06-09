from nltk.parse.corenlp import CoreNLPParser
from nltk import Tree

def getNodes(parent):
    ROOT = 'ROOT'

    for node in parent:
        if type(node) is Tree:
            if node.label() == ROOT:
                print ("======== Sentence =========")
                print ("Sentence:", " ".join(node.leaves()))
            else:
                print ("Label:", node.label())
                print ("Leaves:", node.leaves())

            getNodes(node)
        else:
            print ("Word:", node)


def break_up_sent(node):
    if len(node) == 1 and type(node[0]) is str:
        return [node[0]]
    else:
        # print(node.label())
        contains_cc = False
        for child in node:
            if child.label() == 'CC':
                contains_cc = True
        if contains_cc:
            return_this = []
            for child in node:
                # l += child.label() + " "
                if child.label() != 'CC':
                    result = break_up_sent(child)
                    for i in result:
                        return_this.append(i)
            # l += " YES"
            # print(l)
            return return_this
        else:
            # l = ""
            # for child in node:
            #     l += child.label() + " "
            # l += " NO"
            # print(l)
            return_this = []
            for child in node:
                result = break_up_sent(child)
                if len(return_this) == 0:
                    for i in result:
                        return_this.append(i)
                else:
                    new_rt = []
                    for i in return_this:
                        for j in result:
                            new_rt.append(i + " " + j)
                    return_this = new_rt
            return return_this

        # for child in node:
        #     break_up_sent(child)


parser = CoreNLPParser()

comp_sent_rec = [
    'This is a test sentence',
    'Install v6.1.0 from F-Droid and launch the app.',
    'Click I have a custom server, and input an invalid server address, e.g., xx',
    'Click register or login.',
    'input "t" in the username input box and password input box.',
    'the app would be crashed, and show a word: Unfortunately, Newsblur has stopped',
    'Input "t" into the username and password input box.',
    'log in with username "t" and password "t".',
    'Incorrect username or password,but the software crashed.',
    'Input t on the username input box and password input box.',
    'select some cards and press Start',
    'set foresight period value as any 11 digit number crashed the application',
    'Delete all Data of the App, start it and tell the app that you have a existing Account.',
    'Only Type letters in the username and click on sign in.',
    'Install App and import local SMS from the device.',
    'hey i have a problem and that is after building project when i try to edit the saved video, app crashesh on multiple devices (m above).',
    'During multiple input of identical values e.g. 10 km (by day) and 10 litres some calculations fail. E.g. first calculates correcty 100 l/km but then next two results are \"infinity l / 100 km.',
    'Plotting will death lock program then and you have to restart device.'
]

for sent in comp_sent_rec:
    parse = next(parser.raw_parse(sent))
    t = Tree.fromstring(str(parse))

    t.pretty_print()
    # print(t.leaves())

    result = break_up_sent(t)
    print(result)
    print()

# parse = next(parser.raw_parse("Input t on the username input box and password input box."))
# print(parse)
# t = Tree.fromstring(str(parse))
# t.pretty_print()
