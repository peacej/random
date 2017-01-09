# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    river = {}
    i = 0
    while len(river) < X and i<len(A):

        if A[i] in river:

            pass
        else:
            river[A[i]] = True


        i += 1
    if len(river)==X:
        return i
    else:
        return -1



print('solution is'+str(solution(4,[1,1,1,1,1,1,1])))
