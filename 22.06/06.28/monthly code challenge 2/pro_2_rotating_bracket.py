"""
17분 소요, 스스로 풂
핵심 포인트
1. stack 관리에 주의
"""
def solution(s):
    answer = 0

    def check(bracket):
        stack = []
        for b in bracket:
            if b == ")" and len(stack) > 0 and stack[-1] == "(":
                stack.pop()
                continue
            elif b == "}" and len(stack) > 0 and stack[-1] == "{":
                stack.pop()
                continue
            elif b == "]" and len(stack) > 0 and stack[-1] == "[":
                stack.pop()
                continue
            stack.append(b)
        return True if len(stack) == 0 else False

    for i in range(len(s)):
        if check(s[i:] + s[:i]):
            answer += 1
    return answer