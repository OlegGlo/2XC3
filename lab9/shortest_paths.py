from lab9 import create_random_complete_graph

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
        print("[",nodes[i],"]")
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and c[node] < k:
                    print(node)
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    c[node] += 1
                    pred[neighbour] = node
    return dist

g = create_random_complete_graph(10,10)
bellman_ford_approx(g, 0, 5)