from lab9 import create_random_complete_graph
import min_heap

def bellman_ford_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())
    c = [0]*G.number_of_nodes()

    #Initialize distances
    for node in nodes:
        dist[node] = 99999
    dist[source] = 0

    #Meat of the algorithm
    for i in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and c[node] < k:
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    c[node] += 1
                    pred[neighbour] = node
    return dist

g = create_random_complete_graph(10,10)
bellman_ford_approx(g, 0, 5)

def dijkstra(G, source):
    dist = [] #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, 99999))
        dist.append(99999)
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
    return dist

def all_pairs_dijkstra(G):
    matrix = []
    for node in list(G.adj.keys()):
        matrix.append(dijkstra(G, node))
    return matrix

all_pairs_dijkstra(g)

def bellman_ford(G, source):
    dist = [] #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist.append(99999)
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
    return dist

def all_pairs_bellman_ford(G):
    matrix = []
    for node in list(G.adj.keys()):
        matrix.append(bellman_ford(G, node))
    return matrix

all_pairs_bellman_ford(g)