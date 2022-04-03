"""
7분 소요, 예전 코드 참고함 (시간 초과 남)
핵심 포인트
1. 시간 초과 => stack쓰기 // stack[-1]이랑 현 alphabet 비교해서 pop하고, 다르면 append
"""
def solution(s):
    stack=[]
    for alphabet in s:
        if stack and stack[-1]==alphabet:
            stack.pop()
        else:
            stack.append(alphabet)
    return 1 if len(stack)==0 else 0
