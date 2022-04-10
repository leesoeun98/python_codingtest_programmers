"""
19분 소요, 스스로 풂
핵심 포인트
1. ""에 대해 예외처리 잘하기
2. 순서대로 구현해서 재귀적으로 푸는 연습 하기 (특히 changing 함수)
"""
def solution(p):
    if p == "":
        return p

    def splitBalance(bracket):
        for i in range(1, len(bracket) + 1):
            if bracket[:i].count('(') == bracket[:i].count(')'):
                return ''.join(bracket[:i]),''.join(bracket[i:]) if ''.join(bracket[i:])!="" else ""

    def isRight(bracket):
        stack = []
        for b in bracket:
            if stack and stack[-1] == '(' and b == ')':
                stack.pop()
            else:
                stack.append(b)
        return True if len(stack) == 0 else False

    def makingRight(u, v):
        res = "("
        res += changing(v)
        res += ")"
        for b in u[1:-1]:
            if b == '(':
                res += ')'
            else:
                res += '('
        return res

    def changing(bracket):
        if bracket!= '':
            u, v = splitBalance(bracket)
            if isRight(u):
                return u + changing(v)
            else:
                return makingRight(u, v)
        else:
            return ""

    return changing(p)
print(solution("()))((()"))
