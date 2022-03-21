import random

def create_random_graph(n, c): #nodes, edges
    g = WeightedGraph(n)
    edges = []
    edge = (0,0)

    weights = []
    for x in range(c+1):
        weights.append(x+1)
    random.shuffle(weights)

    # print(weights)

    if c > n*(n-1)/2: #cap max verticies
        c = n*(n-1)/2
    while c > 0:
        while edge[0] == edge[1] or edge in edges or edge[::-1] in edges:
            edge = (random.randint(0,n-1), random.randint(0,n-1))
            # print(edge)
            # print(edge[::-1])
        edges.append(edge)
        # print(edge[0],edge[1])
        g.add_edge(edge[0],edge[1],weights[c])
        c -= 1
    return g

def logtocsv(num,results,filename):
    with open(filename, 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for size of {}".format(index))
        return timeit.repeat("prim2(graph)", setup="from __main__ import prim2, graph", repeat=1, number=1) 

import copy 

i = 10
while (i < 1001):
    for x in range(3):
        testGraph = create_random_graph(i,i*2)

        graph = copy.copy(testGraph)
        logtocsv(i, timer(i)[0], "prim2.csv") #To switch function to test, changer here and in the method.

    i *= 10

i = 5
while (i < 5001):
    for x in range(3):
        testGraph = create_random_graph(i,i*2)

        graph = copy.copy(testGraph)
        logtocsv(i, timer(i)[0], "prim2.csv") #To switch function to test, changer here and in the method.

    i *= 10