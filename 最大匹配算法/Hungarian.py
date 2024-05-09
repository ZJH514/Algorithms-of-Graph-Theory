#!/usr/bin/env python3
# -coding:utf-8-*-
# 匈牙利算法
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def match(pos, adjs, V2, checked):
    for i in range(len(V2)):
        if adjs[pos][i] and not checked[i]:
            # 意思是：本次查找时，pos结点（V1）存在连边的V2中结点 i
            # 如果 i 之前没有被查找过，才能对i进行查找
            # 因为如果没有此限制，递归无法停止
            checked[i] = True
            # 如果V2结点i没有被匹配，或者是，能够通过进一步匹配将原本已经匹配的i结点更换位置
            # 那么说明可以通过某些操作可以使pos, i两个结点都能存在对应的匹配
            # 重新给V2[i] 找匹配项，这里为什么可以这样做呢？
            # 因为若是某两个点已经匹配了
            # 比如x 与 y分别为 V1, V2 两个点集中的点
            # 当此处x 选择与 i 进行匹配，造成y需要重选时，y无法再选i 因为已经是 checked
            # 因此 y 只能选别的点，这样递归下去就是查找，之前匹配是否能拆开
            # 找到别的匹配，给新加入的点让出匹配位置
            if V2[i] == -1 or match(V2[i], adjs, V2, checked):
                V2[i] = pos
                return True  # 找到了（回溯）直接返回
    return False  # 直到最后都无法匹配

def runHungary(len_v1, len_v2, adjs):
    V1 = [False for i in range(len_v1)]
    V2 = [-1 for i in range(len_v2)]  # 表示匹配前驱项
    for i in range(len_v1):
        # 在匹配每一个 v1 中的结点时，都设置：V2中的结点没有被查找过
        # 原因是：如果没有被查找过，而之前的匹配V2又实际存在
        # 那么说明，这个匹配是可以拆开的
        # 后进结点总有机会拆开之前的匹配
        chk = [False for i in range(len_v2)]
        if match(i, adjs, V2, chk):
            V1[i] = True
    return V1, V2  # v1 为v1中结点师傅成功匹配，v2为与v2中每一个结点匹配的结果
#通过 matches 得到邻接矩阵
def getAdjs(matches, x, y):
    adjs = np.zeros((x, y)).astype(int)
    for match in matches:
        i, j = match
        adjs[i][j] = 1
    print(adjs)
    return adjs

if __name__ == "__main__":
    matches = [
        (0, 1), (1, 0), (1, 1), (1, 2), (2, 2), (2, 4), (3, 2), (3, 3), (4, 3)
    ]
    x, y = 5, 5
    adjs = getAdjs(matches, x, y)
    V1, V2 = runHungary(x, y, adjs)

    print("V1 - V2 matches:")
    for i in range(x):
        print("%d: (%d) --- %d" % (V2[i], V1[i], i))
    # 创建图对象
    # 创建图对象
    G = nx.Graph()
    # 添加V1的节点，并标记为V1
    for i in range(x):
        G.add_node(f'V1-{i}', bipartite=0, color='red')

    # 添加V2的节点，并标记为V2
    for i in range(y):
        G.add_node(f'V2-{i}', bipartite=1, color='blue')

    # 根据matches添加边，注意V2的节点标签已经更改
    for v1, v2 in matches:
        G.add_edge(f'V1-{v1}', f'V2-{v2}')

    # 设置节点的颜色
    colors = [G.nodes[n]['color'] for n in G.nodes()]

    # 绘制图形
    pos = nx.bipartite_layout(G, nodes=[f'V1-{i}' for i in range(x)])
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=900, font_size=15, font_color='white')
    plt.show()



