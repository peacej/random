# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def prefixsum(A):
    cum0 = [0] * (len(A)+1)
    #cum1 = [0] * (len(A) + 1)
    for i in range(1, len(A)+1):
        cum0[i] = cum0[i - 1] + int(A[i-1]==0)
  #      cum1[i] = cum1[i - 1] + int(A[i-1]==1)
    return (cum0)


def solution(A):
    pairs=0
    cum0=prefixsum(A)[1:]
    for i in range(len(A)):
        if A[i]==1:
            pairs+=cum0[i]
    if pairs>1000000000:
        return -1
    else:
        return pairs

#print(prefixsum([0,1,0,1,1]))
print(solution([0,1,0,1,1]))