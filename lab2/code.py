import random

collection = []
sizeOfColl = []

def ArrayGen():

    i = 1
    while (i < 1000001):
        array = [random.randint(0,100) for x in range(i)]
        collection.append(array)
        i *= 10

    # for size in range(0, 1000001, 100000):
    #     array = [random.randint(0,100) for x in range(size)]
    #     collection.append(array)
    #     sizeOfColl.append(size)

def Average(lst):
    return sum(lst) / len(lst)

def copy(array):

    arrCpy = array.copy()

    return arrCpy

def logtocsv():
    with open('test.csv', 'a') as f: #'w' for write, 'a' for append
        f.write("1000000")
        f.write(",")
        f.write(str(Average(results)))
        f.write('\n')

def timer():
    if __name__ == '__main__':
        import timeit
        print("timing")
        return timeit.repeat("copy(collection[6])", setup="from __main__ import copy, collection", repeat=100, number=100) #CHANGE from 0 to 6

ArrayGen() #Generate arrays
results = timer() #send string
print("Total results ",results)
print("Average over the results ",Average(results))
logtocsv() #save to database
    





