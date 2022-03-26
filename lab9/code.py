import random
from lab9 import DirectedWeightedGraph
from shortest_paths import bellman_ford, bellman_ford_approx

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G

def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def logtocsv(num,results1,results2,filename):
    with open(filename, 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results1))
        f.write(",")
        f.write(str(results2))
        f.write('\n')

def timer1(index):
    if __name__ == '__main__':
        import timeit
        print("timing for original {}".format(index))
        return timeit.repeat("bellman_ford(graph, 0)", setup="from __main__ import bellman_ford, graph", repeat=1, number=1) 

def timer2(index):
    if __name__ == '__main__':
        import timeit
        print("timing for approximation {}".format(index))
        return timeit.repeat("bellman_ford_approx(graph, 0, k)", setup="from __main__ import bellman_ford_approx, graph, k", repeat=1, number=1) 

import copy 

i = 1
while (i < 40):
    for x in range(3):
        testGraph = create_random_complete_graph(100,1000)

        graph = copy.copy(testGraph)
        k = i
        logtocsv(i, timer1(i)[0], timer2(i)[0], "bellman_ford.csv") #To switch function to test, changer here and in the method.

    i += 1

i = 1
while (i < 40):
    for x in range(3):
        testGraph = create_random_complete_graph(100,1000)

        graph = copy.copy(testGraph)
        k = i
        logtocsv(i, total_dist(bellman_ford(graph, 0)), total_dist(bellman_ford_approx(graph, 0, k)), "bellman_ford_dist.csv") #To switch function to test, changer here and in the method.

    i += 1