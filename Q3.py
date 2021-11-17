import networkx as nx
import matplotlib.pyplot as plt


# get G - graph and return G's connected component
def find_connected_components(G):
    CC_map = {}
    x = [c for c in nx.connected_components(G)]
    for i in range(len(x)):
        CC_map[i] = list(x[i])
    return CC_map


# get G - graph and CC_map - G's connected component
# return False - if G's connected component has a "-" edge
# True otherwise
def inside_cc(G, CC_map):
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
            if check_edge(G, CC, i, j):
                CCG.add_edge(i, j)
    return CCG


def Q3_a(G):
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['label'] == '-']  # dashed edge
    G_t = G.copy()
    G_t.remove_edges_from(esmall)

    CC_map = find_connected_components(G_t)

    if not inside_cc(G, CC_map):
        return False

    CCG = calculate_CC_graph(G, CC_map)
    return nx.is_bipartite(CCG)


def Q3_b():
    G = nx.Graph()
    # the network is about the show Fate\stay Night and the character relations
    # the nodes are the main characters , and the edges are the relationships
    # https://en.wikipedia.org/wiki/List_of_Fate/stay_night_characters

    """
    ******** explanation of nodes and edges , and splitting the coalition ********
    
     the coalitions are :
     "good guys"
        Shirou Emiya(saber oner)
        Rin Tohsaka(archer owner)
        Sakura Matou(rider owner)
        Illya(berserker owner)
     
     "bad guys"
        Kirei Kotomine(gilgamesh owner)
        Sōichirō Kuzuki(caster owner)
            
    """

    G.add_node('Shirou Emiya(saber owner)')
    G.add_node('Rin Tohsaka(archer owner)')
    G.add_node('Sakura Matou(rider owner)')
    G.add_node('Illya(berserker owner)')
    G.add_node('Kirei Kotomine(gilgamesh owner)')
    G.add_node('Sōichirō Kuzuki(caster owner)')

    # Add edges by defining weight and label
    G.add_edge('Shirou Emiya(saber owner)', 'Rin Tohsaka(archer owner)', weight=1, label='+')
    G.add_edge('Shirou Emiya(saber owner)', 'Sakura Matou(rider owner)', weight=1, label='+')
    G.add_edge('Shirou Emiya(saber owner)', 'Illya(berserker owner)', weight=1, label='+')
    G.add_edge('Shirou Emiya(saber owner)', 'Kirei Kotomine(gilgamesh owner)', weight=1, label='-')
    G.add_edge('Shirou Emiya(saber owner)', 'Sōichirō Kuzuki(caster owner)', weight=1, label='-')
    G.add_edge('Rin Tohsaka(archer owner)', 'Illya(berserker oner)', weight=1, label='+')
    G.add_edge('Kirei Kotomine(gilgamesh owner)', 'Rin Tohsaka(archer owner)', weight=1, label='-')
    G.add_edge('Kirei Kotomine(gilgamesh owner)', 'Illya(berserker owner)', weight=1, label='-')
    G.add_edge('Kirei Kotomine(gilgamesh owner)', 'Sōichirō Kuzuki(caster owner)', weight=1, label='+')
    return G


def Q3_c(G):
    pos = nx.spring_layout(G)  # positions for all nodes
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['label'] == '+']  # solid edge
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['label'] == '-']
    nx.draw(G, pos=pos, with_labels=True, node_color="dodgerblue", font_size=15)
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=8, alpha=0.5, edge_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=esmall, width=8, alpha=0.5, edge_color='b')


if __name__ == "__main__":
    G = Q3_b()
    print(Q3_a(G))
    Q3_c(G)
    plt.show()
