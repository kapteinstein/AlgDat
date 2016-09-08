#!/usr/bin/python3

from sys import stdin
from itertools import repeat
from collections import deque

def mergedecks(decks):
    # merge the decks
    ord = ''
    while len(decks) != 1:
        decks.append(merge(decks.popleft(), decks.popleft()))
    for bokstav in decks[0]:
        ord += bokstav[1]
    return(ord)


def merge(A, B):
    # merge A and B, both already sorted lists
    C = []
    A = deque(A)
    B = deque(B)
    while len(A) != 0 and len(B) != 0:
        if A[0][0] <= B[0][0]:
            C.append(A.popleft())
        else:
            C.append(B.popleft())
    if len(A) != 0:
        C += A
    if len(B) != 0:
        C += B
    return(C)

def main():
    # Read input.
    decks = deque([])
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(mergedecks(decks))


if __name__ == "__main__":
    main()
