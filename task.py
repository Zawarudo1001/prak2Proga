import networkx as nx
import matplotlib.pyplot as plt


class Graph:

    def __init__(self):
        self.E = []
        self.V = []
        self.pathlist = []
        self.allSimplePathList = []

    def VertexIndex(self, name):
        for vertex in self.V:
            if vertex[0] == name:
                return self.V.index(vertex)
        return -1

    def addV(self, name, mark, label):
        if self.VertexIndex(name) < 0:
            self.V.append([name, mark, label])

    def addE(self, name1, name2, weight):
        if self.VertexIndex(name1) < 0 or self.VertexIndex(name2) < 0:
            return
        for edge in self.E:
            if edge[0] == name1 and edge[1] == name2:
                return
        self.E.append([name1, name2, weight])

    def editV(self, name, newname):
        ind = self.VertexIndex(name)
        if ind >= 0:
            self.V[ind][0] = newname
            for edge in self.E:
                if edge[0] == name:
                    edge[0] = newname
                elif edge[1] == name:
                    edge[1] = newname

    def editE(self, name1, name2, w):
        for edge in self.E:
            if edge[0] == name1 and edge[1] == name2:
                edge[2] = w

    def delV(self, name):
        ind = self.VertexIndex(name)
        if ind >= 0:
            self.V.pop(ind)
            for edge in self.E[:]:
                if edge[0] == name or edge[1] == name:
                    self.E.remove(edge)

    def delE(self, name1, name2):
        for edge in self.E:
            if edge[0] == name1 and edge[1] == name2:
                self.E.remove(edge)

    def First(self, name):
        for edge in self.E:
            if edge[0] == name:
                return self.VertexIndex(edge[1])
        return -1

    def Next(self, name, start):
        flag = 0
        for edge in self.E:
            if edge[0] == name and edge[1] == start:
                flag = 1
                continue
            if edge[0] == name and flag == 1:
                return self.VertexIndex(edge[1])
        return -1

    def Vertex(self, name, index):
        neighbours = []
        for edge in self.E:
            if edge[0] == name:
                neighbours.append(edge[1])
        try:
            return neighbours[index]
        except IndexError:
            return -1

    def dfs(self, index, start, length):
        self.V[index][1] = True
        self.pathlist.append(self.V[index][0])
        if not (self.V[index][0] == start and length > 1):
            j = self.First(self.V[index][0])
            while j > -1:
                if not self.V[j][1] or (self.V[j][0] == start and length > 0):
                    # рассматриваем простые циклы, исключая петли
                    self.dfs(j, start, length + 1)
                j = self.Next(self.V[index][0], self.V[j][0])
            self.V[index][1] = False
        if len(self.pathlist[:]) > 1:
            self.allSimplePathList.append(self.pathlist[:])
        self.pathlist.pop()

    def doTask(self):
        for vertex in self.V:
            self.dfs(self.V.index(vertex), vertex[0], 0)
        self.allSimplePathList.sort()
        for i in self.allSimplePathList:
            print(i)

    def display(self):
        g = nx.DiGraph()
        for vertex in self.V:
            g.add_node(vertex[0])
        g.add_weighted_edges_from(self.E)
        pos = nx.spring_layout(g)
        nx.draw(g, pos, with_labels=True, font_weight='bold')
        edge_weight = nx.get_edge_attributes(g, 'weight')
        nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_weight)
        plt.show()


TaskGraph = Graph()

TaskGraph.addV('a', False, 0)
TaskGraph.addV('b', False, 0)
TaskGraph.addV('c', False, 0)
TaskGraph.addV('d', False, 0)
TaskGraph.addE('a', 'c', 15)
TaskGraph.addE('a', 'b', 10)
TaskGraph.addE('c', 'd', 7)
TaskGraph.addE('b', 'd', 10)
TaskGraph.addE('c', 'b', 12)
TaskGraph.addE('c', 'a', 11)
TaskGraph.addE('b', 'a', 17)
TaskGraph.addE('b', 'b', 5)
TaskGraph.addE('d', 'c', 10)


TaskGraph.doTask()
TaskGraph.display()
