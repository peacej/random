from random import *
import numpy as np
import datetime
import arrow

def solution(N, A):
    # write your code in Python 2.7
    counters=[0]*N
    max=0
    for i in range(len(A)):
        if 1<=A[i]<=N:
            temp=counters[A[i]-1]+1
            counters[A[i]-1]=temp
            if max<temp: max=temp
        if A[i]==N+1:
            counters=[max]*N
    return counters

before = arrow.utcnow()
print(solution(randrange(50),np.random.randint(100,size=2500000)))
after = arrow.utcnow()
print(after - before)

