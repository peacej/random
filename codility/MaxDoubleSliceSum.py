import sys
def solution(A):
    # write your code in Python 2.7
    minval=sys.maxint
    maxsumending=maxsum=-sys.maxint
    for a in A[1:-1]:
        if a<minval:
            minval=a
        if maxsumending+a-minval<0:
            maxsumending = 0
            minval=0
        else:
            maxsumending=maxsumending+a
        maxsum=max(maxsumending-minval,maxsum)
    return maxsum

