#!/usr/bin/python3

from sys import stdin
import copy

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

def search(A, target, L, R, up):
    m = int((L+R)/2)
    while (A[m] != target):
        if L > R:
            if up:
                return(A[L])
            else:
                return(A[R])
        m = int((L+R)/2)

        if A[m] < target:
            L = m+1
        if A[m] > target:
            R = m-1
    return(A[m])

def find(A, lower, upper):
    # NOTICE: The result must be returned.
    # SKRIV DIN KODE HER
    a = search(A, lower, 0, len(A)-1, 0)
    b = search(A, upper, 0, len(A)-1, 1)
    return((a, b))

def main():
    input_list = []
    #for x in stdin.readline().split():
    #    input_list.append(int(x))
    input_list = [int(i) for i in stdin.readline().split()]

    sorted_list = radix_sort2(input_list)

    for line in stdin:
        word = line.split()
        minimum = int(word[0])
        maximum = int(word[1])
        result = find(sorted_list, minimum, maximum)
        print(str(result[0]) + " " + str(result[1]))


if __name__ == "__main__":
    main()
