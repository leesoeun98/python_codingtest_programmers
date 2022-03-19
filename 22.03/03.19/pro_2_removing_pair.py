"""
20분 고민하다가 예전 풀이 봄 (총 30분 걸림)
핵심 포인트
1. stack쓰기
"""
def solution(s):
    stack=[]
    for alpha in s:
        if len(stack)>0 and stack[-1]==alpha:
            stack.pop()
        else:
            stack.append(alpha)
    return 1 if len(stack)==0 else 0


solution("baabaa")