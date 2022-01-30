def arrayLook(array):
    i = 0
    while (i < len(array)): 
        array[i]
        i += 1

def arrayGenApp(upperLimit): #values in array increasing
    j = 0
    arr = []
    
    while (j < upperLimit):
        arr.append(j)
        j += 1

    return arr

def average(lst):
    return sum(lst) / len(lst)

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        #print(array)
        return timeit.repeat("arrayLook(array)", setup="from __main__ import arrayLook, array", repeat=10, number=5) #from 0 to 6

def logtocsv(num,results):
    with open('lookup.csv', 'a') as f: #'w' for write, 'a' for append
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
    i *= 10
    j *= 10