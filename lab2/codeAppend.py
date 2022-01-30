def arrayGenApp(upperLimit): #values in array increasing
    j = 0
    arr = []
    
    while (j < upperLimit):
        arr.append(1)
        j += 1

    return arr

def timer(index):
    if __name__ == '__main__':
        import timeit
        print("timing for {} runs".format(index))
        return timeit.repeat("arrayGenApp({})".format(index), setup="from __main__ import arrayGenApp", repeat=10, number=5) #from 0 to 6

def average(lst):
    return sum(lst) / len(lst)

def logtocsv(num,results):
    with open('append.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')

i = 1
j = 3
while (i < 1000001):
    logtocsv(i, average(timer(i)))
    logtocsv(j, average(timer(j)))
    
    i *= 10
    j *= 10
