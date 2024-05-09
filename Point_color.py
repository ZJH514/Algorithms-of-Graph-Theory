import networkx as nx
import matplotlib.pyplot as plt

#相邻顶点必须不同颜色
def graph_coloring(graph, colors):
    result = {}
    for node in graph.nodes():
        neighbor_colors = set(result.get(nei) for nei in graph.neighbors(node))
        for color in colors:
            if color not in neighbor_colors:
                result[node] = color
                break
    return result

# 创建图
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (4, 6), (5, 6)])

# 原图绘制
plt.figure(1)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_weight='bold')
plt.title('Original Graph')

# 着色
colors = ['red', 'green', 'blue', 'yellow']
color_mapping = graph_coloring(G, colors)

# 着色结果图绘制
plt.figure(2)
node_colors = [color_mapping.get(node, 'white') for node in G.nodes()]
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=1500, font_weight='bold')
plt.title('Colored Graph')
plt.show()