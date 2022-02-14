
# Timing code from previous labs

i = 10

while (i < 1000001):
    for x in range(5):
        testarray = create_random_list(i)  
        array = testarray.copy()
        logtocsv(i, timer(i)[0])

    i *= 10

def logtocsv(num,results):
    with open('3waymerge.csv', 'a') as f: #'w' for write, 'a' for append
        f.write(str(num))
        f.write(",")
        f.write(str(results))
        f.write('\n')