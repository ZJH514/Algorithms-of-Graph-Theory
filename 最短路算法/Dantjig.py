import sys

maxNum = float('inf')  # 定义一个足够大的数，代表图中两顶点间无边


class Graph:
    def __init__(self, V):
        self.V = V
        # g为二维数组，里面每个元素初始化为无穷大
        self.g = [[maxNum] * V for _ in range(V)]

    def addEdge(self, s, t, w):
        self.g[s][t] = w
        self.g[t][s] = w


class Dantzig:
    def __init__(self, G, v):
        self.G = G
        self.v = v
        self.visited = [False] * G.V
        self.t = [0] * G.V
        self.A = []
        self.T = []

        self._Dantzig(v)  # 算法核心

    def _Dantzig(self, v):
        self.A.append(v)
        if len(self.A) == self.G.V:  # 图中所有顶点均已标记，结束递归
            return
        self.visited[v] = True
        minWeight = sys.maxsize  # 存储当前节点下相邻节点中拥有的最短的边长度
        minV = None  # 存放下一个被标记的顶点
        from_vertex, to_vertex = None, None  # 记录路径
        for i in range(len(self.A)):
            for j in range(self.G.V):
                if not self.visited[j] and self.G.g[self.A[i]][j] != maxNum:
                    temp = self.t[self.A[i]]
                    if temp + self.G.g[self.A[i]][j] < minWeight:
                        minWeight = temp + self.G.g[self.A[i]][j]
                        minV = j
                        from_vertex = self.A[i]
                        to_vertex = j
        self.T.append((from_vertex, to_vertex))
        self.t[minV] = minWeight  # 更新起始点到该点的最短路径值
        self._Dantzig(minV)  # 递归调用即可

    def minLen(self, w):
        return self.t[w]

    def getfrom(self, to):
        for vertex_pair in self.T:
            if vertex_pair[1] == to:
                return vertex_pair[0]

    def showpath(self, w):
        stack = []
        from_vertex = self.getfrom(w)
        while from_vertex != self.v:
            stack.append(from_vertex)
            from_vertex = self.getfrom(from_vertex)
        stack.append(self.v)
        while stack:
            print(stack.pop(), "->", end='')
        print(w)


G = Graph(8)
G.addEdge(0, 1, 2)
G.addEdge(0, 2, 8)
G.addEdge(0, 3, 1)
G.addEdge(1, 2, 6)
G.addEdge(1, 4, 1)
G.addEdge(2, 3, 7)
G.addEdge(2, 4, 4)
G.addEdge(2, 5, 2)
G.addEdge(2, 6, 2)
G.addEdge(3, 6, 9)
G.addEdge(4, 5, 3)
G.addEdge(4, 7, 9)
G.addEdge(5, 6, 4)
G.addEdge(5, 7, 6)
G.addEdge(6, 7, 2)

dantzig = Dantzig(G, 0)

# 输出a到b（即0到7）的最短距离
print('输出a到b（即0到7）的最短距离:',dantzig.minLen(7))
print('最短路径为:')
dantzig.showpath(7)  # 打印路径