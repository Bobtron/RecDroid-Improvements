import sys

from Node import Node

file_name = sys.argv[1]

step_matrix = []
nodes = []
curr_node = 1
graph_matrix = []
for i in range(12):
    graph_matrix.append([0] * 12)

for i in range(5):
    step_matrix.append([-1, -1, -1, -1, -1, -1, -1, -1])

with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1]
        steps = line.split(' ')

        node = Node(line)
        nodes.append(node)

        for step in steps:
            step_matrix[int(step[0])][int(step[2])] = curr_node

        curr_node += 1

for col in range(len(step_matrix[0])):
    string = ""
    for row in range(len(step_matrix)):
        if step_matrix[row][col] != -1:
            string += str(step_matrix[row][col]) + " "
            if len(str(step_matrix[row][col])) == 1:
                string += " "
        else:
            string += "   "
    print(string)

# for line in graph_matrix:
#     print(line)
#
# print()

for line in step_matrix:
    for i in range(1, len(line)):
        if line[i-1] != -1 and line[i] != -1:
            graph_matrix[line[i - 1]][line[i]] += 1

    # for line in graph_matrix:
    #     print(line)
    # print()



for line in graph_matrix:
    print(line)

print("Weights:")
for node in nodes:
    print(node.weight)

# Run DFS

