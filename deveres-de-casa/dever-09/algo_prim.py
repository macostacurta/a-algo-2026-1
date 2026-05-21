import networkx as nx
import matplotlib.pyplot as plt


edges = [
    ('A', 'B', 4), ('A', 'C', 4),
    ('B', 'C', 2), ('B', 'D', 5),
    ('C', 'D', 5), ('C', 'E', 6),
    ('D', 'E', 3), ('D', 'F', 4),
    ('E', 'F', 2)
]

G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)


mst = nx.minimum_spanning_tree(G, algorithm='prim')


plt.figure(figsize=(14, 6))


pos = nx.spring_layout(G, seed=42) 


plt.subplot(1, 2, 1)
plt.title("Grafo Original (Todas as conexões e custos)", fontsize=14)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=16, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)


plt.subplot(1, 2, 2)
plt.title("Rede Otimizada (Algoritmo de Prim)", fontsize=14)

nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=16, font_weight='bold', edge_color='lightgray', style='dashed')

nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='red', width=3)
mst_labels = nx.get_edge_attributes(mst, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=mst_labels, font_size=12, font_color='red')

plt.tight_layout()
plt.savefig('grafo_otimizado.png')