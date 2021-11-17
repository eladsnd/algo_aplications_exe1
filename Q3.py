import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from networkx import gnp_random_graph

"""
1.remove negative edges  
    * find connected components 
        :return as dict  #component : list of nodes
2. ceck if there is a negative edge in a CC
    * yes - unbalanced
    *no -continue
3. build the CC graph 
    * 


"""


def find_connected_components(G):
    CC_map = {}
    x = [c for c in nx.connected_components(G)]
    for i in range(len(x)):
        CC_map[i] = list(x[i])
    return CC_map


def inside_cc(G,CC_map):
    for c in CC_map.keys():
        g = G.subgraph(CC_map[c])
        gsmall = [(u, v) for (u, v, d) in g.edges(data=True) if d['label'] == '-']
        if len(gsmall) > 0:
            return False
    return True


def check_edge(G, CC, i, j):
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['label'] == '-']  # solid edge
    for node1 in CC[i]:
        for node2 in CC[j]:
            if esmall.__contains__((node1, node2)):
                return True
    return False


def calculate_CC_graph(G, CC):
    CCG = nx.Graph()
    CCG.add_nodes_from(list(CC.keys()))
    for i in range(CCG.number_of_nodes()):
        for j in range(i + 1, CCG.number_of_nodes()):
            if check_edge(G,CC, i, j):
                CCG.add_edge(i, j)
    return CCG


def Q3_a(G):
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['label'] == '-']  # dashed edge
    G_t = G.copy()
    G_t.remove_edges_from(esmall)

    CC_map = find_connected_components(G_t)

    if not inside_cc(G,CC_map):
        return False

    CCG = calculate_CC_graph(G, CC_map)
    return nx.is_bipartite(CCG)



if __name__ == "__main__":
    G = nx.Graph()
    # the network is about the show Fate\stay Night and the character relations
    # https://en.wikipedia.org/wiki/List_of_Fate/stay_night_characters
    G.add_node('Shirou Emiya(saber oner)', pos=(2, 10))
    G.add_node('Rin Tohsaka(archer oner)', pos=(4, 9))
    G.add_node('Sakura Matou(rider oner)', pos=(0, 13))
    G.add_node('Illya(buserker oner)', pos=(1.5, 4))
    G.add_node('Kirei Kotomine(gilgamesh oner)', pos=(4, 4))
    G.add_node('Sōichirō Kuzuki(caster oner)', pos=(6, 11))

    # Add edges by defining weight and label
    G.add_edge('Shirou Emiya(saber oner)', 'Rin Tohsaka(archer oner)', weight=1, label='+')
    G.add_edge('Shirou Emiya(saber oner)', 'Sakura Matou(rider oner)', weight=1, label='+')
    G.add_edge('Shirou Emiya(saber oner)', 'Illya(buserker oner)', weight=1, label='+')
    G.add_edge('Shirou Emiya(saber oner)', 'Kirei Kotomine(gilgamesh oner)', weight=1, label='-')
    G.add_edge('Shirou Emiya(saber oner)', 'Sōichirō Kuzuki(caster oner)', weight=1, label='-')
    G.add_edge('Rin Tohsaka(archer oner)', 'Illya(buserker oner)', weight=1, label='+')
    G.add_edge('Kirei Kotomine(gilgamesh oner)', 'Rin Tohsaka(archer oner)', weight=1, label='-')
    G.add_edge('Kirei Kotomine(gilgamesh oner)', 'Illya(buserker oner)', weight=1, label='-')
    G.add_edge('Kirei Kotomine(gilgamesh oner)', 'Sōichirō Kuzuki(caster oner)', weight=1, label='+')

    print(Q3_a(G))


