A=[4,3,2,1,5]
B=[1,0,1,1,0]
def solution(A, B):
    # write your code in Python 2.7
    if len(A)==1:
        return 1
    stack=[0] #add first fish
    for i in range(1,len(A)):
        stack.append(i)
        while len(stack)>=2 and B[stack[-2]]==1 and B[stack[-1]]==0:
            if A[stack[-2]]>=A[stack[-1]]:
                del stack[-1]
            else:
                del stack[-2]
    return len(stack)

print(solution(A,B))