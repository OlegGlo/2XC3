from lab7 import *
from graphs import *

def logtocsv(num,results,filename):
    with open(filename, 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

for edgesNum in range(101):
    succNum = 0
    for sample in range(1000):
        g = create_random_graph(100,edgesNum)
        if (has_cycle(g) == True):
            succNum += 1

    logtocsv(edgesNum, succNum/10, "hascycle.csv")

for edgesNum in range(401):
    succNum = 0
    for sample in range(100):
        g = create_random_graph(100,edgesNum)
        if (is_connected(g) == True):
            succNum += 1

    logtocsv(edgesNum, succNum, "isconnected.csv")