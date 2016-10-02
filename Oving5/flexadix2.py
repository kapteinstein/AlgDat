#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict, deque
import cProfile


def instertion_sort(A):
    # instertion_sort
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while (i > -1) and (A[i] > key):
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key
    return(A)

def randomized_partition(A, lo, hi):
    # ranadomized partition
    i = random.randint(lo, hi)
    A[i], A[hi] = A[hi], A[i]
    return partition(A, lo, hi)

def partition(A, lo, hi):
    # partition for quicksort
    pivot = A[lo]
    left = lo + 1
    right = hi

    done = False
    while not done:
        while left <= right and A[left] <= pivot:
            left += 1
        while left <= right and A[right] >= pivot:
            right -= 1
        if left > right:
            done = True
        else:
            A[left], A[right] = A[right], A[left]

    A[lo], A[right] = A[right], A[lo]

    return(right)

def quicksort(A, lo, hi):
    # quicksort
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)
    return(A)

def counting_sort(A, char_count):
    # counting sort
    count = [0]*26
    output = [0]*len(A)

    for x in A:
        try:
            count[chars.index(itemgetter(char_count)(x))] += 1
        except:
            return(A)

    total = 0
    for i in range(1 ,26):
        count[i] += count[i-1]

    for x in reversed(A):
        count[chars.index((itemgetter(char_count)(x)))] -= 1
        output[count[chars.index(itemgetter(char_count)(x))]] = x

    return(output)

def randix_sort(A, k):
    # radix sort
    for i in reversed(range(k)):
        A = counting_sort(A, i)
    return(A)

def radix_sort2(A, k):
    # try to implement the one from wikipedia
    pass

def merge_lists(A):
    while len(A) != 1:
        A.append(merge(A.popleft(), A.popleft()))
    return(A)


def merge(A, B):
    # merge A and B, both already sorted lists
    C = []
    A = deque(A)
    B = deque(B)
    while len(A) != 0 and len(B) != 0:
        if A[0] <= B[0]:
            C.append(A.popleft())
        else:
            C.append(B.popleft())
    if len(A) != 0:
        C += A
    if len(B) != 0:
        C += B
    return(C)


def flexradix(A, length_of_greatest):

    d = defaultdict()
    to_be_merged = deque([])
    # put ordene i en liste, lenge paa ord som index
    for ord in A:
        try:
            d[len(ord)] += [ord]
        except:
            d[len(ord)] = [ord]

    # velge hvilken sorteringsmetode som er best basert paa listens info
    for key in d:
        n = len(d[key])  # number of elements to sort
        k = key  # wordsize

        if (n < 10) and (n > 1):
            # use insertion sort if the list is short
            to_be_merged.append(instertion_sort(d[key]))
        elif abs(k/n - 1) < 0.5 and k > 5:
            # use quicsort if the list is longer and the wordsize approx n
            to_be_merged.append(quicksort(d[key], 0, len(d[key])-1))
        elif (n >= 10):
            # else use radix sort
            #to_be_merged.append(quicksort(d[key], 0, len(d[key])-1))
            to_be_merged.append(randix_sort(d[key], k))
        else:
            # list of length n is already sorted
            to_be_merged.append(d[key])


    # merge de ferdig sorterte listene med mergesort.
    sorted_list = merge_lists(to_be_merged)
    return(sorted_list[0])

def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        a = line.rstrip()
        strings.append(a.lower())


    pr = cProfile.Profile()
    pr.enable()

    A = flexradix(strings, d)
    #for string in A:
    #    print(string)
    pr.disable()
    pr.print_stats(sort='time')

if __name__ == "__main__":
    main()
