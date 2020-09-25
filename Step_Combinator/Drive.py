import sys
import ModularizedFunc

file_name = sys.argv[1]

adj_mat_graph = {}
nearest_neighbor = {}

with open(file_name, 'r') as file:
    lines = file.readlines()
    for line in lines:
        line = line[:-1]
        args = line.split(',')
        node1 = args[0] + "," + args[1] + "; "
        node2 = args[2] + "," + args[3] + "; "
        score = float(args[4])
        if node1 not in adj_mat_graph.keys():
            adj_mat_graph[node1] = {}
        if node2 not in adj_mat_graph.keys():
            adj_mat_graph[node2] = {}
        # if score < .7:
        adj_mat_graph[node1][node2] = score
        adj_mat_graph[node2][node1] = score

while True:

    # print(adj_mat_graph)

    nearest_neighbor = {}

    for key in adj_mat_graph.keys():
        nearest_neighbor[key] = ModularizedFunc.get_nearest_neighbor(adj_mat_graph, key, 0.82)

    # print(nearest_neighbor)


    to_combine = []
    already_listed = []

    for step in nearest_neighbor.keys():
        if step not in already_listed:
            for other_step in nearest_neighbor[step]:
                if step not in already_listed and other_step not in already_listed and step in nearest_neighbor[other_step]:
                    to_combine.append([step, other_step])
                    already_listed.append(step)
                    already_listed.append(other_step)

    print(to_combine)
    if len(to_combine) == 0:
        break

    for pair in to_combine:
        node1 = pair[0]
        node2 = pair[1]
        ModularizedFunc.merge_node(adj_mat_graph, node1, node2)
        # print(adj_mat_graph)

    # print(adj_mat_graph)

# print(adj_mat_graph)

for key in adj_mat_graph.keys():
    print(key)
