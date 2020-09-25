# <p>Status: <code class="ng-binding">Invalid</code></p>

import sys
import os
import re


folder = sys.argv[1]

filenames = []

for root, dirs, files in os.walk(folder):
    for filename in files:
        # print(filename)
        filenames.append(filename)

statusTypes = {}
duplicates = []

regex = r'<p>Status: <code class="ng-binding">(.+?)<\/code><\/p>'

for filename in filenames:
    with open(folder + '/' + filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            # print(line)
            if re.search(regex, line):
                match = re.search(regex, line)
                # print(filename)
                # print(match.group(1))
                if match.group(1) in statusTypes.keys():
                    statusTypes[match.group(1)] += 1
                    if match.group(1) == 'Duplicate':
                        duplicates.append(filename)
                else:
                    statusTypes[match.group(1)] = 1


duplicates.sort()
print(statusTypes)

print()
for i in duplicates:
    print(i)
