import lab3

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

myarray = lab3.create_random_list(10)
print(myarray)
quicksort_inplace(myarray)
print(myarray)