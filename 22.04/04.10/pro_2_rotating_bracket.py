"""
5분 소요, 스스로 풂
핵심 포인트
1. 괄호가 맞는지 확인하는 함수 작성
2. 왼쪽으로 이동하는 문자열 -> list slicing이용
"""
def solution(s):
    count=0
    def isRight(bracket):
        stack=[]
        for b in bracket:
            if stack and stack[-1]=='[' and b==']':
                stack.pop()
            elif stack and stack[-1]=='(' and b==')':
                stack.pop()
            elif stack and stack[-1]=='{' and b=='}':
                stack.pop()
            else:
                stack.append(b)
        return True if len(stack)==0 else False
    for i in range(len(s)):
        if isRight(s[i:]+s[:i]):
            count+=1
    return count
