def l():
    from sys import stdin
    return(stdin.readlines())
def p(ord):
    print(ord.strip('\n'))
def r(A):
    buckets = [[]]*26
    while len(A) >= 2:
        print(A[0][0])
        if A[0][0].lower() == 'a':
            p(A.pop())
        A.pop()
    p(A)

r(l())
