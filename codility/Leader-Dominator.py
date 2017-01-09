def solution(A):
    # write your code in Python 2.7
    if len(A)==0:
        return -1
    if len(A)==1:
        return 0
    size=0
    for val in A:
        if size==0:
            value=val
            size=1
        elif val==value:
            size+=1
        else:
            size-=1
    valuecount=0
    for i in range(len(A)):
        if value==A[i]:
            valuecount+=1
            resultindex=i
    if valuecount>len(A)/2.0:
        return resultindex
    else:
        return -1