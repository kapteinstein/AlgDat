#!/usr/bin/python3

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []

def bygg(ordliste):
    # build tree from wordlist
    root = Node()
    for o in ordliste:
        node = root
        for bokstav in o[0]:
            if bokstav in node.barn.keys():
                node = node.barn[bokstav]
            else:
                node.barn[bokstav] = Node()
                node = node.barn[bokstav]
        node.posi.append(o[1])
    return(root)


def posisjoner(ord, index, node):
    # find the positions of a word
    pos = []
    if index == len(ord):
        # print(node.posi)
        return(node.posi)
    else:
        try:
            if ord[index] == '?':
                for key in node.barn.keys():
                    pos += posisjoner(ord, index + 1, node.barn[key])
            else:
                pos += posisjoner(ord, index + 1, node.barn[ord[index]])
        except:
            return([])
    return(pos)


def main():
    try:
        ord = stdin.readline().split()
        ordliste = []
        pos = 0
        for o in ord:
            ordliste.append((o, pos))
            pos += len(o) + 1
        toppnode = bygg(ordliste)
#        print(toppnode.barn['h'].barn['a'].posi)
        for sokeord in stdin:
            sokeord = sokeord.strip()
            print("{}:".format(sokeord), end='')
            posi = posisjoner(sokeord, 0, toppnode)
            #print(posi)
            posi.sort()
            for p in posi:
                print(" {}".format(p), end='')
            print()
    except:
        traceback.print_exc(file=stderr)


if __name__ == "__main__":
    main()

