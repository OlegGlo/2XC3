def prim1(graph):

    mst = WeightedGraph(graph.number_of_nodes()) #create new graph
    pqueueEdge = list()
    pqueueNode = list()
    pqueue = list()
    marked = set()
    node = 0

    visit(graph, pqueueEdge, pqueueNode, pqueue, marked, mst, node)

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

def visit(graph, pqueueEdge, pqueueNode, pqueue, marked, mst, node):
    marked.add(node)
    for x in graph.adjacent_nodes(node):
        if x[0] not in marked:
            pqueue.append((node,x[0],x[1]))
            # pqueueEdge.append(x)
            # pqueueNode.append(node)
            # print(x)

def prim2(graph):
        nodes = graph.number_of_nodes()
        mst = WeightedGraph(nodes)
        inf = 1e7
         
        key = [0]
        L = [Element(0,0)] 
        parent = [-1]

        for n in range(1,nodes):
            parent.append(-1) #-1 is questionable
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
            if(parent[n]!=-1): #accounting for disconnected graph
                mst.add_edge(parent[n],n,key[n])
        
        return mst