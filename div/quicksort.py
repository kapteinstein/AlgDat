def partition(A, lo, hi):
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
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p-1)
        quicksort(A, p+1, hi)

def main():
    l = [1,4,3,5,76,5,3]
    quicksort(l, 0, len(l)-1)
    print(l)

if __name__ == '__main__':
    main()
