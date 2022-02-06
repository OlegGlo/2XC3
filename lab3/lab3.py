import random
import math

import sys
print(sys.getrecursionlimit())

def my_quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]

    print(1)


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
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)


def create_random_list(n):
    L = []
    for _ in range(n):
        L.append(random.randint(1,n))
    return L


def create_near_sorted_list(n, factor):
    L = create_random_list(n)
    for i in range(0,factor):
        L.sort()
        print(i/10)
        for _ in range(math.ceil(n*i/10)):
            index1 = random.randint(0, n-1)
            index2 = random.randint(0, n-1)
            L[index1], L[index2] = L[index2], L[index1]
        print(L)
    return L
    
def swap(L, i, j):
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def insertion_sort(L):
    for i in range(1, len(L)):
        insert_into(L, i)

def insert_into(L, n):
    i = n
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i, i-1)
        else:
            return
        i -= 1

def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]): # i is the index of the previous element
            return False
    return True

def dual_pivot_quicksort(L,c):
    copy = quicksort_2pivot(L,c)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_2pivot(L,c):
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
    c += 1    
    final = quicksort_2pivot(left,c) + [pivotL] + quicksort_2pivot(mid,c) + [pivotR] + quicksort_2pivot(right,c)
    print(c)
    return final



array = [x for x in range(200)]
print(array)
dual_pivot_quicksort(array,0)
print(array)