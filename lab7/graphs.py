from collections import deque
from lab7 import Graph, BFS, DFS
import random

def backtrack(parent, node1, node2):
    path = [node2]
    while path[-1] != node1:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def BFS2(G, node1, node2):
    Q = deque([node1])
    parent = {}
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                parent[node] = current_node
                return backtrack(parent, node1, node2)
            if not marked[node]:
                parent[node] = current_node
                Q.append(node)
                marked[node] = True
    return []

def DFS2(G, node1, node2):
    S = [node1]
    parent = {}
    marked = {}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True
    while len(S) != 0:
        current_node = S.pop()
        for node in G.adj[current_node]:
            if not marked[node]:
                marked[node] = True
                parent[node] = current_node
                S.append(node)
                if node == node2:
                    return backtrack(parent, node1, node2)
    return []

def BFS3(G, node1):
    Q = deque([node1])
    parent = {}
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if not marked[node]:
                parent[node] = current_node
                Q.append(node)
                marked[node] = True
    return parent

def DFS3(G, node1):
    S = [node1]
    parent = {}
    marked = {}
    for node in G.adj:
        marked[node] = False
    marked[node1] = True
    while len(S) != 0:
        current_node = S.pop()
        for node in G.adj[current_node]:
            if not marked[node]:
                marked[node] = True
                parent[node] = current_node
                S.append(node)
    return parent

def has_cycle(G):
    for i in G.adj:
        S = [i]
        parent = {}
        marked = {}
        for node in G.adj:
            marked[node] = False
        while len(S) != 0:
            current_node = S.pop()
            marked[current_node] = True
            for node in G.adj[current_node]:
                if not marked[node]:
                    parent[node] = current_node
                    S.append(node)
                elif parent[current_node] != node:
                    return True
    return False


def is_connected(G):
    if len(DFS3(G,0)) == len(G.adj)-1:
        return True
    else: return False

def create_random_graph(n, c): #nodes, edges
    g = Graph(n)
    edges = []
    edge = (0,0)
    if c > n*(n-1)/2: 
        c = n*(n-1)/2
    while c > 0:
        while edge[0] == edge[1] or edge in edges or edge[::-1] in edges:
            edge = (random.randint(0,n-1), random.randint(0,n-1))
        edges.append(edge)
        g.add_edge(edge[0],edge[1])
        c -= 1
    return g

def print_graph(G):
    for node in G.adj:
        print(node)
        print(G.adj[node])

<<<<<<< HEAD
z = Graph(4)
z.add_edge(0,3)
z.add_edge(0,1)
z.add_edge(2,3)

y = Graph(3)
y.add_edge(0,1)
y.add_edge(0,2)
y.add_edge(1,2)

x = Graph(5)
x.add_edge(0,3)
x.add_edge(0,1)
x.add_edge(2,3)

print(has_cycle(z))
print(is_connected(z))
print(has_cycle(y))
print(is_connected(y))
print(has_cycle(x))
print(is_connected(x))
=======
g = create_random_graph(6,6)
print_graph(g)
print("\n\n")
print(is_connected(g))
print(has_cycle(g))

# z = Graph(4)
# z.add_edge(0,3)
# z.add_edge(0,1)
# z.add_edge(2,3)
# print_graph(z)
# print(has_cycle(z))
>>>>>>> 28e55698b33d9359a32dd818f3d92f0a9a3a2d0a
