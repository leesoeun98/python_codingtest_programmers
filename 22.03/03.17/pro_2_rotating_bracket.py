"""
푸는덴 25분 걸렸으나, 예전에 푼 괄호 stack 풀이 참고함
=> 괄호 stack은 외우기
"""
def solution(s):
    def isRight(str):
        stack = []
        for s in str:
            if s == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(s)
            elif s == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(s)
            else:
                stack.append(s)
        return True if len(stack) == 0 else False

    count = 0
    for i in range(len(s)):
        s = s[1:] + s[0]
        if (isRight(s)):
            count += 1
    return count