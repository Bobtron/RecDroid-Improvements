import sys
import re

filename = sys.argv[1]

regex = r'<issues:status>Duplicate<\/issues:status>(?:.*?)<id>http:\/\/code\.google\.com\/feeds\/issues\/p\/android\/issues\/full\/(\d+)<\/id>'

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        # print(line)
        if re.search(regex, line):
            match = re.search(regex, line)
            # print(filename)
            print(match.group(1))
            # if match.group(1) in statusTypes.keys():
            #     statusTypes[match.group(1)] += 1
            #     if match.group(1) == 'Duplicate':
            #         duplicates.append(filename)
            # else:
            #     statusTypes[match.group(1)] = 1