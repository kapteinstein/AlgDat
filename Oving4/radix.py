import math
import copy
from sys import stdin
import timeit


def mergesort(A, p, r):
    '''Sort an unsorted list using mergesort'''
    if p < r:
        q = floor((p + r)/2)
        mergesort(A, p, q)
        mergesort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    '''Merge two sorted lists'''
    n1 = q - p + 1
    n2 = r - q
    L = [0]*(n1 + 1)
    R = [0]*(n2 + 1)

    for i in range(n1):
        L[i] = A[p + i]
    for j in range(n2):
        R[j] = A[q + j + 1]

    L[n1] = 10000000
    R[n2] = 10000000
    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def radix_sort(A):
    l2 = [0]*len(A)
    bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for mod in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        for i in A:
            bucket[int((i/mod) % 10)] += 1
        if bucket[0] == len(A):
            break
        for i in range(1, 10):
            bucket[i] += bucket[i - 1]
        for i in reversed(A):
            a = int((i/mod) % 10)
            bucket[a] -= 1
            l2[bucket[a]] = i
        A = copy.copy(l2)
        bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return(l2)

def radix_sort2(A):
    l2 = [0]*len(A)
    bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for mod in [1, 10, 100, 1000, 10000, 100000, 1000000]:
        for i in A:
            if i < mod:
                bucket[0] += 1
                continue
            else:
                bucket[int((i/mod) % 10)] += 1
        if bucket[0] == len(A):
            break
        for i in range(1, 10):
            bucket[i] += bucket[i - 1]
        for i in reversed(A):
            a = int((i/mod) % 10)
            bucket[a] -= 1
            l2[bucket[a]] = i
        A = copy.copy(l2)
        bucket = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return(l2)

def sorter(A):
    length = len(A)
    sortert_radix = True
    sortert_merge = True


    # start sorteringen
    start_radix = timeit.default_timer()
    l1 = radix_sort2(A)
    stop_radix = timeit.default_timer()

    for i in range(1, length):
        if l1[i] < l1[i-1]:
            sortert_radix = False

#    start_merge = timeit.default_timer()
#    l1 = mergesort(A, 0, len(A)-1)
#    stop_merge = timeit.default_timer()
#
#    # sjekker om lista er sortert
#    for i in range(1, length):
#        if l1[i] < l1[i-1]:
#            sortert_merge = False
    print('')
    print('Sortert: {}'.format(sortert_radix))
    print(' Length: {}'.format(length))
    print('   Time: {}'.format(stop_radix-start_radix))

def main():
    #liste = [1,554,2,334,7,5,128,6,9]
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
    sorter(input_list)

if __name__ == '__main__':
    main() 
