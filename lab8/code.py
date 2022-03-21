#Undirected graph using an adjacency list
class WeightedGraph:

    weightSet = set()

    def __init__(self, n):
        self.weightSet.clear() #Set tracking addition
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        for edge in self.adj[node1]:
            if edge[0] == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2, weight):
        if weight not in self.weightSet:
            self.weightSet.add(weight) # Prevent equal weights
            
            if node1 not in self.adj[node2]:
                self.adj[node1].append((node2, weight))
                self.adj[node2].append((node1, weight))
        else:
            print("duplicate weights")

    def w(self, node1, node2):
        for edge_info in self.adj[node1]:
            if node2 == edge_info[0]:
                return edge_info[1]

    def number_of_nodes(self):
        return len(self.adj)

    def showWeights(self):
        for x in self.weightSet:
            print(x)

    def show(self):
        for i in range(len(self.adj)):
            print("node:", i)
            print(self.adj[i])

def primsBasic(graph):

    mst = WeightedGraph(graph.number_of_nodes()) #create new graph
    pqueueEdge = list()
    pqueueNode = list()
    pqueue = list()
    marked = set()
    node = 0

    # mst.show()

    # print(pqueueNode, " - ", pqueueEdge)
    # print(pqueue)
    # print(marked)
    # print(node)

    visit(graph, pqueueEdge, pqueueNode, pqueue, marked, mst, node)
    # # pqueue.sort(key=lambda tup: tup[1])#sorts based on weights
    # visit(graph, pqueueEdge, pqueueNode, pqueue, marked, mst, node+1)

    # print(pqueueNode, " - ", pqueueEdge)
    # print(pqueue)
    # print(marked)
    # print(node)



    #add current node parameter
    while(len(pqueue)!= 0):
        pqueue.sort(key=lambda tup: tup[2]) #sorts based on weights
        minEdge = pqueue.pop(0)

        if (minEdge[0] in marked and minEdge[1] in marked):
            continue #this vertix is marked or the other one is
        
        mst.add_edge(minEdge[0],minEdge[1],minEdge[2]) #add connection to completed mst
        if (minEdge[0] not in marked):
            visit(graph, pqueueEdge, pqueueNode, pqueue, marked, mst, minEdge[0])
        if (minEdge[1] not in marked):
            visit(graph, pqueueEdge, pqueueNode, pqueue, marked, mst, minEdge[1])

    return mst

def findMin(list): #didnt use
    minNum = 0
    return minNum

def visit(graph, pqueueEdge, pqueueNode, pqueue, marked, mst, node):
    marked.add(node)
    for x in graph.adjacent_nodes(node):
        if x[0] not in marked:
            pqueue.append((node,x[0],x[1]))
            # pqueueEdge.append(x)
            # pqueueNode.append(node)
            # print(x)
    
mst = primsBasic(gr1)
mst.show()

import math

class MinHeap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.map = {}
        for i in range(len(L)):
            self.map[L[i].value] = i
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.sink(i)

    def sink(self, i):
        smallest_known = i
        if self.left(i) < self.length and self.data[self.left(i)].key < self.data[i].key:
            smallest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)].key < self.data[smallest_known].key:
            smallest_known = self.right(i)
        if smallest_known != i:
            self.data[i], self.data[smallest_known] = self.data[smallest_known], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[smallest_known].value] = smallest_known
            self.sink(smallest_known)

    def insert(self, element):
        if len(self.data) == self.length:
            self.data.append(element)
        else:
            self.data[self.length] = element
        self.map[element.value] = self.length
        self.length += 1
        self.swim(self.length - 1)

    def insert_elements(self, L):
        for element in L:
            self.insert(element)

    def swim(self, i):
        while i > 0 and self.data[i].key < self.data[self.parent(i)].key:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            self.map[self.data[i].value] = i
            self.map[self.data[self.parent(i)].value] = self.parent(i)
            i = self.parent(i)

    def get_min(self):
        if len(self.data) > 0:
            return self.data[0]
  
    def extract_min(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.map[self.data[self.length - 1].value] = self.length - 1
        self.map[self.data[0].value] = 0
        min_element = self.data[self.length - 1]
        self.length -= 1
        self.map.pop(min_element.value)
        self.sink(0)
        return min_element

    def decrease_key(self, value, new_key):
        if new_key >= self.data[self.map[value]].key:
            return
        index = self.map[value]
        self.data[index].key = new_key
        self.swim(index)

    def get_element_from_value(self, value):
        return self.data[self.map[value]]

    def get_key_from_value(self, value):
        return self.data[self.map[value]].key

    def is_empty(self):
        return self.length == 0
    
    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

class Element:

    def __init__(self, value, key):
        self.value = value
        self.key = key

    def __str__(self):
        return "(" + str(self.value) + "," + str(self.key) + ")"

def prim2(graph):
        nodes = graph.number_of_nodes()
        mst = WeightedGraph(nodes)
        inf = 1e7
         
        key = [0]
        L = [Element(0,0)] 
        parent = [-1]

        for n in range(1,nodes):
            parent.append(-1)
            key.append(inf)
            L.append(Element(n,inf))
        
        minHeap = MinHeap(L)
        minHeap.length = nodes
 
        while not minHeap.is_empty():
            current = minHeap.extract_min()
            
            for adj in graph.adjacent_nodes(current.value):
                v = adj[0]
                
                try:
                    minHeap.get_element_from_value(v)
                except KeyError:
                    continue
                if adj[1] < key[v]:
                    key[v] = adj[1]
                    parent[v] = current.value
                    minHeap.decrease_key(v, key[v])
        
        for n in range(1,nodes):
            mst.add_edge(parent[n],n,key[n])
        
        return mst