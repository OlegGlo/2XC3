
#An example code used for testing and timing

import math

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap1()
        # self.build_heap2()
        # self.build_heap3()

    def build_heap1(self):
        for i in range(self.length // 2 - 1, -1, -1): 
            # print(i)
            self.sink(i)
            
    def build_heap2(self):
        temp = self.data
        length = self.length
        self.data = []
        self.length = 0
        for i in range(length):
            self.insert(temp[i])

    def build_heap3(self):
        while not self.is_heap():
            for i in range(self.length//2-1):
                self.sink(i)
            # print(self)

    def is_heap(self):
        for i in range(self.length//2-1):
            if not (self.data[i]>=self.data[self.left(i)] and self.data[i]>=self.data[self.right(i)]):
                return False
        return True

    def sink(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            # print(self.left(i))
            # print(self.data[i])
            # print(self.data[self.left(i)])
            largest_known = self.left(i)
        # print(self.right(i))
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            # print(self.right(i))
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i] #swap values without temp value
            self.sink(largest_known) #

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.sink(0)
        return max_value

    def left(self, i):
        # return 2 * (i + 1) - 1
        return 2 * i + 1

    def right(self, i):
        # return 2 * (i + 1)
        return 2 * i + 2

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s


import random

def createRandom(length):
    array = []

    for x in range(length):
        array.append(x)

    random.shuffle(array)
    
    return array


def logtocsv(num,results):
    with open('heap1.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')


def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        return timeit.repeat("Heap(array)", setup="from __main__ import Heap, array", repeat=1, number=1) 


def isHeap(arr, n):
     
    # Start from root and go till
    # the last internal node
    for i in range(int((n - 2) / 2) + 1):
         
        # If left child is greater,
        # return false
        if arr[2 * i + 1] > arr[i]:
                return False
 
        # If right child is greater,
        # return false
        if (2 * i + 2 < n and
            arr[2 * i + 2] > arr[i]):
                return False
    return True

#For isHeap testing

# array = [1,2,3,4,5,6]
# print(array)
# print(isHeap(array,len(array)))


# h = Heap(array)
# print(array)
# print(isHeap(array, len(array)))


i = 10

while (i < 1000001):
    for x in range(5):
        testarray = createRandom(i)
        # print(testarray)
        # print(isHeap(testarray, len(testarray))) 

        array = testarray.copy()
        logtocsv(i, timer(i)[0])

        # print(array)
        # print(isHeap(array, len(array))) 
        
    i *= 10