#!/usr/bin/python3
# -*- coding: utf-8 -*-

from sys import stdin

def left(i):
    return(2*i + 1)
def right(i):
    return(2*i + 2)

def lagTre(A, root, y, LC, RC):
    if A[root] == '-':
        A[root] = [-1, -1]
        return
    if right(root) < len(A):
        lagTre(A, left(root), y+2, LC-1, RC)
        lagTre(A, right(root), y+2, LC, RC+1)
    A[root] = [LC+RC, y]

def shift(A):
    mi = 0
    for koo in A:
        if koo[1] != -1 and koo[0] < mi:
            mi = koo[0]
    for koo in A:
        if koo[1] != -1:
            koo[0] -= mi

def main():
    A = stdin.readline().strip().split(" ")
    lagTre(A, 0, 0, 0, 0)
    shift(A)
    print(A, end='')


if __name__ == "__main__":
    main()
