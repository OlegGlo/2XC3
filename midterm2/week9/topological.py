# Directed unweighted graph using an adjacency list
class DirectedGraph:

    def __init__(self):
        self.adj = {}

    def are_connected(self, node1, node2):
        for edge in self.adj[node1]:
            if edge == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2):
        if node2 not in self.adj[node2]:
            self.adj[node1].append(node2)

    def number_of_nodes(self):
        return len(self.adj)


G = DirectedGraph()

for i in range(8):
    G.add_node(i)

G.add_edge(0,1)
G.add_edge(1,2)
G.add_edge(1,6)
G.add_edge(1,7)
G.add_edge(2,3)
G.add_edge(3,1)
G.add_edge(3,5)
G.add_edge(3,7)
G.add_edge(5,4)
G.add_edge(4,3)
G.add_edge(7,6)





# Depth First Search

def DFS(G, root):
    colours = {}
    for i in range(G.number_of_nodes()):
        colours[i] = "white"
    DFS_visit(G, root, colours)

def DFS_visit(G, node, colours):
    colours[node] = "cyan"
    print("Colouring cyan: " + str(node))
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            DFS_visit(G, neighbour, colours)
    colours[node] = "crimson"
    print("Colouring crimson: " + str(node))


def topo_sort(G):
    nodes = list(G.adj.keys())
    colours = {}
    sched = []
    for node in nodes:
        colours[node] = "white"
    for node in nodes:
        if colours[node] == "white":
            topo_visit(G, node, colours, sched)
    sched.reverse()
    return sched


def topo_visit(G, node, colours, sched):
    colours[node] = "cyan"
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            topo_visit(G, neighbour, colours, sched)
    colours[node] = "crimson"
    sched.append(node)

def get_transpose(G):
    GT = DirectedGraph()
    for node in G.adj:
        GT.add_node(node)
    for source in G.adj:
        for target in G.adj[source]:
            GT.add_edge(target, source)
    return GT


def SCC(G):
    components = []
    stack = []
    GT = get_transpose(G)
    print(GT.adj)
    SCC_DFS(G, stack)
    print(stack)
    return SCC_util(GT, stack)


def SCC_util(GT, stack):
    colours = {}
    component = []
    components = []
    for node in stack:
        colours[node] = "white"
    while stack != []:
        if colours[stack[-1]] == "grey":
            stack.pop()
        else:
            find_component(GT, stack[-1], colours, component)
            components.append(component)
            component = []
    return components


def find_component(G, node, colours, component):
    colours[node] = "grey"
    print("Visiting: " + str(node))
    component.append(node)
    for neighbour in G.adj[node]:
        print(str(node) + "->" + str(neighbour))
        if colours[neighbour] == "white":
            find_component(G, neighbour, colours, component)


def SCC_DFS(G, stack):
    nodes = list(G.adj.keys())
    colours = {}
    for node in nodes:
        colours[node] = "white"
    for node in nodes:
        if colours[node] == "white":
            SCC_DFS_visit(G, node, colours, stack)


def SCC_DFS_visit(G, node, colours, stack):
    colours[node] = "grey"
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            SCC_DFS_visit(G, neighbour, colours, stack)
    colours[node] = "black"
    stack.append(node)

# DFS(G,0)
# print (topo_sort(G))

# stck = []
# SCC_DFS(G,stck)
# print(stck)
# print("asd")
print(SCC(G))



# G = DirectedGraph()

# G.add_node("prep lecture")
# G.add_node("relearn material")
# G.add_node("wake up")
# G.add_node("coffee")
# G.add_node("shower")
# G.add_node("get dressed")
# G.add_node("teach")
# G.add_node("brush beard")
# G.add_node("feed dog")
# G.add_node("sleep")

# G.add_edge("sleep", "wake up")
# G.add_edge("wake up", "shower")
# G.add_edge("wake up", "coffee")
# G.add_edge("coffee", "teach")
# G.add_edge("shower", "get dressed")
# G.add_edge("shower", "brush beard")
# G.add_edge("brush beard", "teach")
# G.add_edge("get dressed", "teach")
# G.add_edge("wake up", "shower")
# G.add_edge("relearn material", "prep lecture")
# G.add_edge("prep lecture", "teach")
# G.add_edge("wake up", "feed dog")
# G.add_edge("teach", "sleep")



















"""

G = DirectedGraph()

G.add_node("wake up")
G.add_node("coffee")
G.add_node("shower")
G.add_node("get dressed")
G.add_node("teach")
G.add_node("prep lecture")
G.add_node("relearn material")



G.add_edge("wake up", "shower")
G.add_edge("wake up", "coffee")
G.add_edge("coffee", "teach")
G.add_edge("shower", "get dressed")
G.add_edge("get dressed", "teach")
G.add_edge("wake up", "shower")
G.add_edge("relearn material", "prep lecture")
G.add_edge("prep lecture", "teach")

 nodes = list(G.adj.keys())
    colours = {}
    for node in nodes:
        colours[node] = "white"
    DFS_visit(G, root, colours)

colours[node] = "grey"
    print("grey:" + str(node))
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            DFS_visit(G, neighbour, colours)
    print("black:" + str(node))
    colours[node] = "black"

# Depth First Search
def DFS(G, root):
    nodes = list(G.adj.keys())
    colours = {}
    for node in nodes:
        colours[node] = "white"
    DFS_visit(G, root, colours)


def DFS_visit(G, node, colours):
    colours[node] = "grey"
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            DFS_visit(G, neighbour, colours)
    print(node)
    colours[node] = "black"

def topological_sort(G):
    nodes = list(G.adj.keys())
    colours = {}
    values = []
    for node in nodes:
        colours[node] = "white"
    for node in nodes:
        if colours[node] == "white":
            topo_visit(G, node, colours, values)
    values.reverse()
    return values

def topo_visit(G, node, colours, values):
    colours[node] = "grey"
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            topo_visit(G, neighbour, colours, values)
    colours[node] = "black"
    values.append(node)


def get_transpose(G):
    GT = DirectedGraph()
    for node in G.adj:
        GT.add_node(node)
    for source in G.adj:
        for target in G.adj[source]:
            GT.add_edge(target, source)
    return GT


def SCC(G):
    components = []
    stack = []
    GT = get_transpose(G)
    print(GT.adj)
    SCC_DFS(G, stack)
    print(stack)
    return SCC_util(GT, stack)


def SCC_util(GT, stack):
    colours = {}
    component = []
    components = []
    for node in stack:
        colours[node] = "white"
    while stack != []:
        if colours[stack[-1]] == "grey":
            stack.pop()
        else:
            find_component(GT, stack[-1], colours, component)
            components.append(component)
            component = []
    return components


def find_component(G, node, colours, component):
    colours[node] = "grey"
    print("Visiting: " + str(node))
    component.append(node)
    for neighbour in G.adj[node]:
        print(str(node) + "->" + str(neighbour))
        if colours[neighbour] == "white":
            find_component(G, neighbour, colours, component)


def SCC_DFS(G, stack):
    nodes = list(G.adj.keys())
    colours = {}
    for node in nodes:
        colours[node] = "white"
    for node in nodes:
        if colours[node] == "white":
            SCC_DFS_visit(G, node, colours, stack)


def SCC_DFS_visit(G, node, colours, stack):
    colours[node] = "grey"
    for neighbour in G.adj[node]:
        if colours[neighbour] == "white":
            SCC_DFS_visit(G, neighbour, colours, stack)
    colours[node] = "black"
    stack.append(node)


G = DirectedGraph()

G.add_node("wake up")
G.add_node("coffee")
G.add_node("shower")
G.add_node("get dressed")
G.add_node("teach")
G.add_node("prep lecture")
G.add_node("relearn material")

G.add_edge("wake up", "shower")
G.add_edge("wake up", "coffee")
G.add_edge("coffee", "teach")
G.add_edge("shower", "get dressed")
G.add_edge("get dressed", "teach")
G.add_edge("wake up", "shower")
G.add_edge("relearn material", "prep lecture")
G.add_edge("prep lecture", "teach")

G_SCC = DirectedGraph()
for i in range(10):
    G_SCC.add_node(i)

G_SCC.add_edge(0, 1)
G_SCC.add_edge(1, 2)
G_SCC.add_edge(2, 3)
G_SCC.add_edge(3, 0)
G_SCC.add_edge(2, 4)
G_SCC.add_edge(4, 5)
G_SCC.add_edge(5, 6)
G_SCC.add_edge(6, 4)
G_SCC.add_edge(6, 7)
G_SCC.add_edge(8, 0)
G_SCC.add_edge(9, 8)
G_SCC.add_edge(8, 9)

"""