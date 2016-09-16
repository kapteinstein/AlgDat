import math
import copy
from sys import stdin
import timeit

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

def sorter(A):
    length = len(A)
    sortert = True


    # start sorteringen
    start = timeit.default_timer()
    l1 = radix_sort(A)
    stop = timeit.default_timer()

    # sjekker om lista er sortert
    for i in range(1, length):
        if l1[i] < l1[i-1]:
            sortert = False

    print('Sortert: {}'.format(sortert))
    print(' Length: {}'.format(length))
    print('   Time: {}'.format(stop-start))

def main():
    #liste = [1,554,2,334,7,5,128,6,9]
    input_list = []
    for x in stdin.readline().split():
        input_list.append(int(x))
    sorter(input_list)

if __name__ == '__main__':
    main() 
