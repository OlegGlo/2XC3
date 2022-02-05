def my_quicksort(L):

    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
        
    final = quicksort_copy(left) + [pivot] + quicksort_copy(right)
    return final

#NO COPY PUT HERE

def dual_pivot_quicksort(L):
    copy = quicksort_2pivot(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_2pivot(L):
    if len(L) < 2:
        return L
    pivotL = L[0]
    pivotR = L[-1]
    if (pivotL >= pivotR):
        temp = pivotL
        pivotL = pivotR
        pivotR = temp
    left, right, mid = [], [], []
    for num in L[1:-1]:
        if num < pivotL:
            left.append(num)
        elif pivotL <= num and num <= pivotR:
            mid.append(num)
        else:
            right.append(num)
        
    final = quicksort_2pivot(left) + [pivotL] + quicksort_2pivot(mid) + [pivotR] + quicksort_2pivot(right)
    return final

def tri_pivot_quicksort(L):
    copy = quicksort_3pivot(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_3pivot(L):
    if len(L) < 2:
        return L
    if len(L) == 2:
        L.sort()
        return L
    temp = []
    temp.append(L[0])
    temp.append(L[1])
    temp.append(L[-1])
    temp.sort()
    pivotL = temp[0]
    pivotM = temp[1]
    pivotR = temp[2]
    
    left, right, midL, midR = [], [], [], []
    for num in L[2:-1]:
        if num < pivotL:
            left.append(num)
        elif pivotL <= num and num <= pivotM:
            midL.append(num)
        elif pivotM <= num and num <= pivotR:
            midR.append(num)
        else:
            right.append(num)
        
    final = quicksort_3pivot(left) + [pivotL] + quicksort_3pivot(midL) + [pivotM] + quicksort_3pivot(midR) + [pivotR] + quicksort_3pivot(right)
    return final

def quad_pivot_quicksort(L):
    copy = quicksort_4pivot(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_4pivot(L):
    if len(L) < 2:
        return L
    if len(L) < 4:
        L.sort()
        return L
    temp = []
    temp.append(L[0])
    temp.append(L[1])
    temp.append(L[-2])
    temp.append(L[-1])
    temp.sort()
    pivotL = temp[0]
    pivotML = temp[1]
    pivotMR = temp[2]
    pivotR = temp[3]
    
    left, right, midL, midM, midR = [], [], [], [], []
    for num in L[2:-2]:
        if num < pivotL:
            left.append(num)
        elif pivotL <= num and num <= pivotML:
            midL.append(num)
        elif pivotML <= num and num <= pivotMR:
            midM.append(num)
        elif pivotMR <= num and num <= pivotR:
            midR.append(num)
        else:
            right.append(num)
        
    final = quicksort_4pivot(left) + [pivotL] + quicksort_4pivot(midL) + [pivotML] + quicksort_4pivot(midM) + [pivotMR] + quicksort_4pivot(midR) + [pivotR] + quicksort_4pivot(right)
    return final