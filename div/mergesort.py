from math import floor
import random

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

    L[n1] = 10000
    R[n2] = 10000
    i = 0
    j = 0

    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1


def main():
#    liste = [2,4,8,7,8,1,2,3]
    liste = []
    for i in range(100):
        liste.append(random.randint(0, 1000))
    mergesort(liste, 0, liste.__len__() - 1)
    print(liste)

if __name__ == '__main__':
    main()
