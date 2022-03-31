import random

def edgeListForGraph(g):
    edges = []
    for i in range(g.number_of_nodes()):
        for j in g.adjacent_nodes(i):
            edges.append((i,j))

    for edge in edges:
        a = edge[0]
        b = edge[1]
        # print(a,b)
        for check in edges:
            if (a == check[1] and b == check[0]):
                edges.remove((check[0],check[1]))
    return edges

def vc_approx1(g): #add type

    Cov = set()
    Edges = edgeListForGraph(g)

    while (len(Edges) != 0):

        ranEdge = random.choice(Edges) #can also replace with node 0

        Cov.add(ranEdge[0])
        Cov.add(ranEdge[1])


        if ( len(g.adjacent_nodes(ranEdge[0])) >= len(g.adjacent_nodes(ranEdge[1]))):
            for i in g.adjacent_nodes(ranEdge[0]):
                try:
                    Edges.remove((ranEdge[0],i))
                    # print("removing edge", ranEdge[0], i)
                except:
                    pass
                try:
                    Edges.remove((i,ranEdge[0]))
                    # print("removing edge", i, ranEdge[0])
                except:
                    pass
        else:
            for j in g.adjacent_nodes(ranEdge[1]):
                
                try:
                    Edges.remove((ranEdge[1],j))
                    # print("removing edge", ranEdge[1], j)
                except:
                    pass
                try:
                    Edges.remove((j,ranEdge[1]))        
                    # print("removing edge", j, ranEdge[1])
                except:
                    pass

    vCover = list(Cov)
    return vCover

def vc_approx2(): #add type
    return

def driver():

    vc_approx1()

    vc_approx2()
    
    return