import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli


def create_first_iteration(N, k):
    G = nx.Graph()
    G.add_nodes_from([i for i in range(N)])
    for i in range(N):
        for j in range(1, int(k / 2) + 1):
            G.add_edge(i, (i + j) % N)
            G.add_edge(i, (i - j) % N)
    nx.draw(G)
    return G


def Watts_Strogantsz_model(N, k, p):
    G = create_first_iteration(N, k)
    non_edge = list(nx.complement(G).edges())
    non_edge_size = len(non_edge)
    for edge in G.edges():
        if bernoulli(p):
            add = np.random.randint(0, non_edge_size)
            G.add_edge(non_edge[add][0], non_edge[add][1])
            non_edge[add] = edge
            G.remove_edge(edge[0], edge[1])
    return G


def clustering_coefficient_of_node(G, node):
    k = G.degree(node)
    if k < 2:
        return 0
    neighbors = [node for node in G.neighbors(node)]
    neighbors_sub_graph = G.subgraph(neighbors)
    neighbors_num_of_edes = len(neighbors_sub_graph.edges())
    return 2 * neighbors_num_of_edes / (k * (k - 1))


def clustering_coefficient(G):
    sum = 0
    for node in G.nodes():
        sum += clustering_coefficient_of_node(G, node)
    return sum / len(G.nodes())


if __name__ == '__main__':
    plt.figure(0)
    G = Watts_Strogantsz_model(20, 6, 0.5)
    plt.figure(1)
    nx.draw(G)
    print("the clustering coefficient is : " + str(round(clustering_coefficient(G),2)))
    plt.show()
