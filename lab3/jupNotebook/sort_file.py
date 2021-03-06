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

def quicksort_inplace(L, left=0, right=None):
    if (right == None):
        right = len(L)-1
    if (left < right):
        p = partition(L, left, right)
        quicksort_inplace(L, left, p-1)
        quicksort_inplace(L, p+1, right)
    else: 
        return
    
def partition(L, left, right):
    pivot = L[left]
    n = right+1
    for i in range(right,left,-1):
        if (L[i]>pivot):
            n -= 1
            L[n], L[i] = L[i], L[n]
    L[n-1], L[left] = L[left], L[n-1]
    return n-1

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

def final_sort(L):

    copy = final_sorting(L)
    for i in range(len(L)):
        L[i] = copy[i]

def final_sorting(L):
    if len(L) < 2:
        return L
    if len(L) < 10:
        insertion_sort(L)
        return L
    else:
        pivot = median(L[0],L[-1],L[int(len(L)/2)])
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return final_sorting(left) + [pivot] + final_sorting(right)

def insertion_sort(L):
    for i in range(1, len(L)):
        insert_into(L, i)

def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i-1]:
            L[i], L[i-1] = L[i-1], L[i]
        else:
            return
        i -= 1

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def median(a,b,c):
    x = biggest(a,b,c)
    if x == a:
        return bigger(b,c)
    if x == b:
        return bigger(a,c)
    else:
        return bigger(a,b)