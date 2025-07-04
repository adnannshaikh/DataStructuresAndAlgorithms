# #Edge list
# graph = [[0,2],[2,3],[2,1],[1,3]]
#
# # Adjecent List
# #index is the node and the value is the nodes neighbours
# graph2 = [[2],[2,3],[0,1,3],[1,2]]
#
# # Adjecent Matrix
# # 0s and 1s x has connection to node y or naah
# graph3 = [
#     [0,0,1,0],
#     [0,0,1,1],
#     [1,1,0,1],
#     [0,1,1,0]
# ]

class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def addVertex(self,node):
            self.adjacent_list[node] = []
            self.number_of_nodes += 1
    def addEdge(self,node1,node2):
        self.adjacent_list[node1].append(node2)
        self.adjacent_list[node2].append(node1)

    def show_connections(self):
        for node in self.adjacent_list:
            connections = " ".join(self.adjacent_list[node])
            print(f"{node} --> {connections}")


g = Graph()
g.addVertex('0')
g.addVertex('1')
g.addVertex('2')
g.addVertex('3')
g.addVertex('4')
g.addVertex('5')
g.addVertex('6')
g.addEdge('3','1')
g.addEdge('3','4')
g.addEdge('0','1')
g.addEdge('0','2')
g.addEdge('2','1')
g.addEdge('2','4')
# g.addEdge('1','3')
# g.addEdge('1','2')
# g.addEdge('4','3')
g.addEdge('4','5')
g.addEdge('5','6')
g.show_connections()




