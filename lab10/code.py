from lab10.lab10 import *
from vertex_cover import *

def graphConstructor(n):
    #n - nodes

    # m = int( n*((n-1)/2) * 0.25)
    m = n * 2
    if (m > int( n*((n-1)/2))):
        m = int( n*((n-1)/2))

    print ("vertices:",n)
    print ("edges:", m)

    graph = create_random_graph(n,m)

    return graph

def find_minimal_cover(g):

    minimal = list(range(500000)) #max size of list

    for i in range(500):
        current = list()
        current = vc_approx1(g)

        if (len(current) < len(minimal)):
            minimal = current

    return minimal

def run10(f,g):

    total = 0
    avg = 0

    for _ in range(10):
        current = f(g)
        total += len(current)

    avg = (total/10)

    return avg

def logtocsv(samplesSize,run10,minimal,filename):
    with open(filename, 'a') as f: #'w' for write, 'a' for append
        f.write(str(samplesSize))
        f.write(",")
        f.write(str(run10))
        f.write(",")
        f.write(str(minimal))
        f.write('\n')

def timing():
    i = 1
    while (i < 21): #701 is as far as i went

        graph = graphConstructor(i)

        logtocsv(i,run10(vc_approx3,graph),len(vertex_cover(graph)),"VC3approx.csv")

        if (i < 102):
            i += 1
        else:
            i += 30

# timing()

g = graphConstructor(5)
g.number_of_nodes()