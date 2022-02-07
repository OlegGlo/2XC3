
from sort_file import my_quicksort
from sort_file import dual_pivot_quicksort
from sort_file import tri_pivot_quicksort
from sort_file import quad_pivot_quicksort
from sort_file import quicksort_inplace

import random

dataPoints = 5

def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L

#FOR NO COPY PIVOT

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        return timeit.repeat("quicksort_inplace(array)", setup="from __main__ import quicksort_inplace, array", repeat=1, number=1) #from 0 to 6

def logtocsv(num,results):
    with open('nocopy.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

i = 10
print("timing in place")

while (i < 1000001):
    for x in range(dataPoints):
        testarray = create_random_list(i) 
        array = testarray.copy()
        logtocsv(i, timer(i)[0])

    i *= 10

#FOR 1 PIVOT

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        return timeit.repeat("my_quicksort(array)", setup="from __main__ import my_quicksort, array", repeat=1, number=1) #from 0 to 6

def logtocsv(num,results):
    with open('1pivot.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

i = 10
print("timing 1 pivot")

while (i < 1000001):
    for x in range(dataPoints):
        testarray = create_random_list(i) 
        array = testarray.copy()
        logtocsv(i, timer(i)[0])

    i *= 10

#FOR 2 PIVOT

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        return timeit.repeat("dual_pivot_quicksort(array)", setup="from __main__ import dual_pivot_quicksort, array", repeat=1, number=1) #from 0 to 6

def logtocsv(num,results):
    with open('2pivot.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

i = 10
print("timing 2 pivot")

while (i < 1000001):
    for x in range(dataPoints):
        testarray = create_random_list(i) 
        array = testarray.copy()
        logtocsv(i, timer(i)[0])

    i *= 10

#FOR 3 PIVOT

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        return timeit.repeat("tri_pivot_quicksort(array)", setup="from __main__ import tri_pivot_quicksort, array", repeat=1, number=1) #from 0 to 6

def logtocsv(num,results):
    with open('3pivot.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

i = 10
print("timing 3 pivot")

while (i < 1000001):
    for x in range(dataPoints):
        testarray = create_random_list(i) 
        array = testarray.copy()
        logtocsv(i, timer(i)[0])

    i *= 10

#FOR 4 PIVOT

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        return timeit.repeat("quad_pivot_quicksort(array)", setup="from __main__ import quad_pivot_quicksort, array", repeat=1, number=1) #from 0 to 6

def logtocsv(num,results):
    with open('4pivot.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

i = 10
print("timing 4 pivot")

while (i < 1000001):
    for x in range(dataPoints):
        testarray = create_random_list(i) 
        array = testarray.copy()
        logtocsv(i, timer(i)[0])

    i *= 10