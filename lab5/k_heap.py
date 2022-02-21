import math

class Heap:
    length = 0
    data = []

    def __init__(self, L, k):
        self.k_value = k
        self.data = L
        self.length = len(L)
        self.build_heap(self.data)

    def build_heap(self,values):
        for i in range(self.length // self.k_value - 1, -1, -1): 
            # print(i)
            self.sink(i)

    def parent(self,i):
        return (i - 1) // self.k_value

    def children(self,i):
        childlist = []
        for indices in range(1,self.k_value+1):
            childlist.append((self.k_value * i) + indices)
        return childlist

    def sink(self, i):
        largest_known = i
        for indices in range(len(self.children(i))):
            # print(self.children(i))
            if self.children(i)[indices] < self.length and self.data[self.children(i)[indices]] > self.data[i]:
                if (self.data[self.children(i)[indices]] > self.data[largest_known]):
                    largest_known = self.children(i)[indices]
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.sink(largest_known)
    
    def output(self):
        print(self.data)

    def __str__(self):
        self.output()
        # height = math.ceil(math.log(self.length + 1, 2))
        # whitespace = 2 ** height
        # s = ""
        # for i in range(height):
        #     for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
        #         s += " " * whitespace
        #         s += str(self.data[j]) + " "
        #     s += "\n"
        #     whitespace = whitespace // 2
        # return s