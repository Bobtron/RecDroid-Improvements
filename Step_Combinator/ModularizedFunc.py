

def get_nearest_neighbor(adj_mat_graph, node):
    neighbors = []
    closest_score = 2 # worst score can only be 1
    for neighbor in adj_mat_graph[node].keys():
        if adj_mat_graph[node][neighbor] < closest_score:
            neighbors = [neighbor]
            closest_score = adj_mat_graph[node][neighbor]
        elif adj_mat_graph[node][neighbor] == closest_score:
            neighbors.append(neighbor)

    return neighbors


def merge_node(adj_mat_graph, node1, node2):
    node1_neighbors = adj_mat_graph[node1]
    node2_neighbors = adj_mat_graph[node2]
    for node in node1_neighbors.keys():
        del adj_mat_graph[node][node1]
    for node in node2_neighbors.keys():
        del adj_mat_graph[node][node2]
    merged = node1 + node2
    adj_mat_graph[merged] = {}
    for node in node1_neighbors.keys():
        if node in node2_neighbors.keys():
            adj_mat_graph[merged][node] = max(node1_neighbors[node], node2_neighbors[node])
    for node in adj_mat_graph[merged].keys():
        adj_mat_graph[node][merged] = adj_mat_graph[merged][node]
    del adj_mat_graph[node1]
    del adj_mat_graph[node2]
