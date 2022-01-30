import random

def copy(array):

    arrCpy = array.copy()

    return arrCpy

def arrayGenApp(upperLimit):
    j = 0
    arr = []

    while (j < upperLimit):
        arr.append(random.randint(0,upperLimit))
        j += 1

    return arr

def average(lst):
    return sum(lst) / len(lst)

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        #print(array)
        return timeit.repeat("copy(array)", setup="from __main__ import copy, array", repeat=10, number=5) #from 0 to 6

def logtocsv(num,results):
    with open('copy.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

i = 1
j = 3
while (i < 1000001):
    array = arrayGenApp(i)
    logtocsv(i, average(timer(i)))

    array = arrayGenApp(j)
    logtocsv(j, average(timer(j)))

    j *= 10
    i *= 10
