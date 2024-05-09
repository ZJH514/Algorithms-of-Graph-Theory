import matplotlib.pyplot as plt
import networkx as nx
class Kruskal:
    def __init__(self, vertices):
        self.vertices = vertices
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}
        self.minimum_spanning_tree = []

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

    def kruskal(self, edges):
        sorted_edges = sorted(edges, key=lambda edge: edge[2])

        for edge in sorted_edges:
            u, v, weight = edge
            if self.find(u) != self.find(v):
                self.minimum_spanning_tree.append(edge)
                self.union(u, v)

        return self.minimum_spanning_tree

# Example Usage:

vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 4),
    ('A', 'C', 6),
    ('B', 'C', 2),
    ('B', 'D', 9),
    ('C', 'D', 7),
    ('C', 'E', 8),
    ('D', 'E', 3)
]
kruskal = Kruskal(vertices)
minimum_spanning_tree = kruskal.kruskal(edges)
print('最小生成树为:\n',minimum_spanning_tree)

####绘制原图G
G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)
# 绘制图形
pos = nx.spring_layout(G)
nx.draw_networkx(G, pos)
# 绘制边的权值
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
# 显示图形
plt.show()

'''绘制最小生成树
T = nx.DiGraph()
for u, v, w in minimum_spanning_tree:
    T.add_edge(u, v, weight=w)
# 绘制图形
pos = nx.spring_layout(T)
nx.draw_networkx(T, pos)
# 绘制边的权值
labels = nx.get_edge_attributes(T, 'weight')
nx.draw_networkx_edge_labels(T, pos, edge_labels=labels)
# 显示图形
plt.show()'''
