# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(K, A):
    # write your code in Python 2.7
    minval=min(A)
    maxval=max(A)
    result=0
    dic={}
    for i in range(minval,maxval+1):
        dic[i]=0
    for item in A:
        dic[item]=dic[item]+1
    for key in dic:
        if (K-key) in dic:
            result+=dic[key]*dic[K-key]
    return result


print(solution(-3, [1, 8, -3, 0, 1, 3]))