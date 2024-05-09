
import matplotlib.pyplot as plt
from collections import defaultdict 
import networkx as nx


class Graph: 

    def __init__(self,vertices): 
        self.V= vertices
        self.graph = defaultdict(list)
        self.Time = 0


    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u) 


    def rmvEdge(self, u, v): 
        for index, key in enumerate(self.graph[u]): 
            if key == v: 
                self.graph[u].pop(index) 
        for index, key in enumerate(self.graph[v]): 
            if key == u: 
                self.graph[v].pop(index) 

    def DFSCount(self, v, visited): 
        count = 1
        visited[v] = True
        for i in self.graph[v]: 
            if visited[i] == False: 
                count = count + self.DFSCount(i, visited)        
        return count 

    def isValidNextEdge(self, u, v): 

        if len(self.graph[u]) == 1: 
            return True
        else:
            visited =[False]*(self.V) 
            count1 = self.DFSCount(u, visited)
            self.rmvEdge(u, v) 
            visited =[False]*(self.V) 
            count2 = self.DFSCount(u, visited) 

            self.addEdge(u,v)
            return False if count1 > count2 else True


    def printEulerUtil(self, u):
        for v in self.graph[u]:
            if self.isValidNextEdge(u, v): 
                print("%d-%d " %(u,v)), 
                self.rmvEdge(u, v) 
                self.printEulerUtil(v) 

    def printEulerTour(self):
        u = 0
        for i in range(self.V): 
            if len(self.graph[i]) %2 != 0 : 
                u = i 
                break
        print ("\n") 
        self.printEulerUtil(u)

####图1####
g1 = nx.DiGraph()
g1.add_edge(0, 1)
g1.add_edge(0, 2)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
plt.figure(1)
pos = nx.spring_layout(g1)
nx.draw_networkx(g1, pos)
# 绘制边的权值
labels = nx.get_edge_attributes(g1, 'weight')
nx.draw_networkx_edge_labels(g1, pos, edge_labels=labels)
# 显示图形
g1 = Graph(4)
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.printEulerTour() 


####图2####
g2 = nx.DiGraph()
g2.add_edge(1, 0)
g2.add_edge(0, 2)
g2.add_edge(2, 1)
g2.add_edge(0, 3)
g2.add_edge(3, 4)
g2.add_edge(3, 2)
g2.add_edge(3, 1)
g2.add_edge(2, 4)
plt.figure(2)
pos = nx.spring_layout(g2)
nx.draw_networkx(g2, pos)
# 绘制边的权值
plt.figure(1)
labels = nx.get_edge_attributes(g2, 'weight')
nx.draw_networkx_edge_labels(g2, pos, edge_labels=labels)
# 显示图形
g2 = Graph (5)
g2.addEdge(1, 0)
g2.addEdge(0, 2)
g2.addEdge(2, 1)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(3, 2)
g2.addEdge(3, 1)
g2.addEdge(2, 4)
g2.printEulerTour()

plt.show()