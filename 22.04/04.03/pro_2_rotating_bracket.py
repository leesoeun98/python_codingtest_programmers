"""
6분 소요, 스스로 풂
핵심 포인트
1. 서로 다른 종류의 bracket이 있을 때도 right한 지 check 구현 능력
2. 문자열 index slicing으로 회전 구현하기
"""
def solution(s):
    candidate=[]
    def isRight(bracket):
        stack=[]
        for b in bracket:
            if stack and stack[-1]=='(' and b==')':
                stack.pop()
            elif stack and stack[-1]=='{' and b == '}':
                stack.pop()
            elif stack and stack[-1]=='[' and b==']':
                stack.pop()
            else:
                stack.append(b)
        return True if len(stack)==0 else False
    for i in range(len(s)):
        candidate.append(isRight(s[i:]+s[:i]))
    return candidate.count(True)