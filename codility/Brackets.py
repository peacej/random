
def solution(S):
    # write your code in Python 2.7
    map={'}':'{',']':'[',')':'('}
    stack=[]
    for item in S:
        if item in '[({':
            stack.append(item)
        elif len(stack)>=1 and stack[-1]==map[item]:
            stack.pop()
        else:
            return 0
    if len(stack)==0:
        return 1
    else:
        return 0