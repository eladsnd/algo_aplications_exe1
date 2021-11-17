import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx import gnp_random_graph


def degree_centrality_node(G, node):
    return G.degree(node)


def num_of_sortest_paths_containing_node(node, paths):
    sum = 0
    for p in paths:
        if node in p:
            sum += 1
    return sum


def betweenness_centrality_node(G, node):
    summ = 0
    # double loop for every 2 nodes
    for start_node in G.nodes():
        for end_node in G.nodes():
            # ignore the node if it is at the edge
            if start_node == end_node or start_node == node or end_node == node:
                continue
            #     create lists of the paths
            shortest_paths = [p for p in nx.all_shortest_paths(G, source=start_node, target=end_node)]
            # by the formula add the relative number of listse containing node to the number of lists
            summ += num_of_sortest_paths_containing_node(node, shortest_paths) / len(shortest_paths)
    # we counted twice so divide
    return summ / 2


def closeness_centrality_node(G, node):
    length = nx.shortest_path_length(G, node)
    summ = 0
    for node2 in G.nodes():
        summ += length[node2]
    if summ > 0:
        return 1 / summ
    else:
        return 0


# def Q2_a():
#     G = nx.karate_club_graph()
#     G = nx.Graph()
#     G.add_edges_from([(0, 1)
#                          , (0, 2)
#                          , (0, 3)
#                          , (0, 4)
#                          , (0, 5)
#                          , (0, 6)
#                       ])
#     print(closeness_centrality_node(G, 0))
#     print(betweenness_centrality_node(G, 0))
#     print(degree_centrality_node(G, 0))
#
#     print("test_case")
#     print(nx.closeness_centrality(G))
#     print(nx.betweenness_centrality(G))
#     print(nx.degree_centrality(G))


def max_Closness(G, flag):
    map = {}
    for node in G.nodes():
        map[node] = closeness_centrality_node(G, node)
    if flag == 1:
        output = sorted(map, key=map.__getitem__, reverse=True)
        return output[0:3]
    else:
        return dict(sorted(map.items(), key=lambda item: item[1], reverse=True))


def max_Betweeness(G, flag):
    map = {}
    for node in G.nodes():
        map[node] = betweenness_centrality_node(G, node)
    if flag == 1:
        output = sorted(map, key=map.__getitem__, reverse=True)
        return output[0:3]
    else:
        return dict(sorted(map.items(), key=lambda item: item[1], reverse=True))


def max_Degree(G, flag):
    map = {}
    for node in G.nodes():
        map[node] = degree_centrality_node(G, node)
    if flag == 1:
        output = sorted(map, key=map.__getitem__, reverse=True)
        return output[0:3]
    else:
        return dict(sorted(map.items(), key=lambda item: item[1], reverse=True))


def Q2_b(G):
    print("top nodes by Degree : " + str(max_Degree(G, 1)))
    print("top nodes by Betweenes : " + str(max_Betweeness(G, 1)))
    print("top nodes by Closeness : " + str(max_Closness(G, 1)))


def Q2_c(G):
    Cb = max_Betweeness(G, 2)
    Cc = max_Closness(G, 2)
    Cd = max_Degree(G, 2)
    plt.figure("closeness_centrality", figsize=(20, 10))
    nx.draw(G, with_labels=True, node_color="teal", font_size=15, node_size=[v * 55000 for v in Cc.values()])
    plt.figure("degree_centrality", figsize=(20, 10))
    nx.draw(G, with_labels=True, node_color="skyblue", font_size=15, node_size=[v * 500 for v in Cd.values()])
    plt.figure("betweenness_centrality", figsize=(20, 10))
    nx.draw(G, with_labels=True, node_color="dodgerblue", font_size=15, node_size=[v * 500 for v in Cb.values()])
    plt.show()


if __name__ == "__main__":
    G = gnp_random_graph(22, p=0.3)
    Q2_b(G)
    Q2_c(G)
