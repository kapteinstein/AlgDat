#!/usr/bin/python3

from sys import stdin
from string import ascii_lowercase as chars
from random import randint, choice
from operator import itemgetter
from collections import defaultdict
import cProfile


def flexradix(A, d):
    """
    This one permits words of length zero as well -- though we might not want
    that, if we use empty lines as separators.
    """
    n = len(A)

    # Count how many words exist of each length:
    B = [0] * (d + 1)
    for word in A:
        B[len(word)] += 1

    # Make B reverse cumulative -- how many are *at least* this long?
    for j in range(d-1, -1, -1):
        B[j] += B[j+1]

    # Using counting sort by length:
    A = counting_sort_length(A)

    # From last to first possible character: Sort those who have it by that
    # character:
    for j in range(d, 0, -1):
        # In-place counting sort by letters:
        A[n-B[j]:] = counting_sort_letters(A[n-B[j]:], j-1)
    return A


def counting_sort_length(A):
    B, C = [], defaultdict(list)           # Output and "counts"
    for x in A:
        C[len(x)].append(x)              # "Count" len(x)
    for k in range(min(C), max(C)+1):      # For every key in the range
        B.extend(C[k])                     # Add values in sorted order
    return B


def counting_sort_letters(A, position):
    B, C = [], defaultdict(list)           # Output and "counts"
    for x in A:
        C[x[position]].append(x)           # "Count" position (x)
    if C:
        for k in range(ord(min(C)), ord(max(C))+1):      # For every key in the range
            B.extend(C[chr(k)])                          # Add values in sorted order
    return B
# SLUTT IKKE-UTDELT KODE


def main():
    d = int(stdin.readline())
    strings = []
    for line in stdin:
        strings.append(line.rstrip())

    pr = cProfile.Profile()
    pr.enable()

    A = flexradix(strings, d)
    #for string in A:
    #    print(string)
    pr.disable()
    pr.print_stats(sort='time')

if __name__ == "__main__":
    main()
