def heapsort(A):
    def heapify(A):
        start = (len(A)-2) // 2
        while start >= 0:
            siftdown(A, start, len(A) - 1)
            start -= 1

    def siftdown(A, start, end):
        root = start
        while root * 2 + 1 <= end:
            child = root * 2 + 1
            if child + 1 <= end and A[child] < A[child + 1]:
                child += 1
            if child <= end and A[root] < A[child]:
                A[root], A[child] = A[child], A[root]
                root = child
            else:
                return

    heapify(A)
    end = len(A) - 1
    while end > 0:
        A[0], A[end] = A[end], A[0]
        siftdown(A,0,end-1)
        end -= 1

def solution(A):
    heapsort(A)
    return max(A[0]*A[1]*A[-1],A[-1]*A[-2]*A[-3])

A=[-4, -6, 3, 4, 5]
heapsort(A)
print(A)


#print(solution([-4, -6, 3, 4, 5] ))