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
    for node1 in G.adj:
        for node2 in G.adj:
            if node1 != node2 and BFS(G, node1, node2):
                if BFS2(G, node1, node2) != DFS2(G, node1, node2):
                    return True
    return False

def is_connected(G):
    for node1 in G.adj:
        for node2 in G.adj:
            if node1 != node2 and not BFS(G, node1, node2):
                return False
    return True

def create_random_graph(n, c):
    g = Graph(n)
    edges = []
    edge = (0,0)
    while c > 0:
        while edge[0] == edge[1] or edge in edges:
            edge = (random.randint(0,n-1), random.randint(0,n-1))
        edges.append(edge)
        g.add_edge(edge[0],edge[1])
        c -= 1
    print(edges)
    return g

def print_graph(G):
    for node in G.adj:
        print(node)
        print(G.adj[node])

g = create_random_graph(3,3)
print_graph(g)
print("\n\n")
print(is_connected(g))
print(has_cycle(g))