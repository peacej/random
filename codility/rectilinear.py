def solution(K, L, M, N, P, Q, R, S):
    # write your code in Python 2.7
    xoverlap=0
    yoverlap=0
    a=S-L
    b=S-Q
    c=N-L
    d=N-Q
    e=M-K
    f=R-P
    g=R-K
    h=M-P
    if S>L and N>Q:
        yoverlap=min(S-L,S-Q,N-L,N-Q)
    if R>K and M>P:
        xoverlap=min(M-K,R-P,R-K,M-P)
    overlap=xoverlap*yoverlap

    print(overlap)
    result= (N-L)*(M-K)+(S-Q)*(R-P)-overlap
    if result>=2147483647:
        return -1
    else:
        return result
#K, L, M, N, P, Q, R, S)
print(solution(-4, 1, 100, 6, 0, -1, 4, 3))