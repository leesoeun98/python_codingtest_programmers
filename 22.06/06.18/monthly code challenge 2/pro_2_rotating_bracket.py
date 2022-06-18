"""
5분 소요, 스스로 풂
1. rotate하기 (slicing 이용)
2. isRight 확인 pop 혹은 append
"""

def solution(s):
    ans = 0

    def isRight(bracket):
        stack = []
        for b in bracket:
            if b == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(b)
            elif b == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(b)
            elif b == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(b)
            else:
                stack.append(b)
        return True if len(stack) == 0 else False

    for i in range(len(s)):
        if isRight(s[i:] + s[:i]):
            ans += 1
    return ans