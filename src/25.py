from collections import defaultdict
import networkx as nx

fo = open("../data/25.txt", "r")
f = list(fo)
fo.close()

adj = defaultdict(list)

for l in f:
    l = l.strip()
    n, neighbors = l.split(': ')
    neighbors = neighbors.split(' ')
    
    for neighbor in neighbors:
        adj[n].append(neighbor)
        adj[neighbor].append(n)

nodes = list(adj.keys())
G = nx.Graph()
G.add_nodes_from(nodes)
for key in adj:
    for n in adj[key]:
        G.add_edge(key, n)

cut = nx.minimum_edge_cut(G)

G.remove_edges_from(cut)

components = list(nx.connected_components(G))

print(len(components[0]) * len(components[1]))

