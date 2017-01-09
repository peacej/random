H=[8, 8, 5, 8, 9,8, 9, 10, 8]
def solution(H):
    # write your code in Python 2.7
    if len(H)==1:
        return 1
    blocks_saved=0    
    stack=[H[0]]
    for i in range(len(H)-1):
        stack.append(H[i+1])
        if len(stack)>=2 and stack[-1]==stack[-2]:
            blocks_saved+=1
            stack.pop()
        else:
            while len(stack)>=2 and stack[-1]<stack[-2]:
                del stack[-2]
                if len(stack)>=2 and stack[-1]==stack[-2]:
                    blocks_saved+=1
                    stack.pop()
    return len(H)-blocks_saved

print(solution(H))