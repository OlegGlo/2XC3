def mergesort_three(L):
    
    if len(L) <= 1:
        return 

    left = list(split(L,3))[0]
    mid = list(split(L,3))[1]
    right = list(split(L,3))[2]

    #Mergesort core
    mergesort_three(left)
    mergesort_three(mid)
    mergesort_three(right)
    
    temp = merge_three(left, mid)
    final = merge_three(temp, right)

    #Copy the sorted list to L
    for i in range(len(final)):
        L[i] = final[i]


def merge_three(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        #Check it there's still elements to be merged from left and/or right
        if i >= len(left): #if an element of one list are exhausted
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else: #if left bigger or equal to right
                L.append(right[j])
                j += 1
    return L

def mergesort_bottom(L):
    w = 1
    while (w < len(L)):
        start = 0
        while (start < len(L)):
            end = min(start + (w*2-1), len(L)-1)
            mid = (start + end)//2
            if (w > len(L)//2):
                mid = end - (len(L) % w)
            merge_bottom(L, start, mid, end)
            start += w*2
        w *= 2
    return L

def merge_bottom(L, start, mid, end):
    l, r = [], []
    a, b = mid - start + 1, end - mid
    for i in range(0,a):
        l.append(L[start + i])
    for i in range(0,b):
        r.append(L[mid + i + 1])

    x, y, z = 0, 0, start
    while (x < a and y < b):
        if l[x] > r[y]:
            L[z] = r[y]
            y += 1
        else:
            L[z] = l[x]
            x += 1
        z += 1
    while (x < a):
        L[z] = l[x]
        x += 1
        z += 1
    while (y < b):
        L[z] = r[y]
        y += 1
        z += 1
    return

#no recursion, only lists