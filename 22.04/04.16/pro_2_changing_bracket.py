"""
16분 소요, 예전 코드 봄
핵심 포인트
1. "" 처리 잘하기 => splitBalance, subSolution
2. makingRight에서 v 붙일 때 subSolution(v) 로 하기
3. 재귀 주의
"""
def solution(p):
    if p == "":
        return p

    def splitBalance(bracket):
        for i in range(1, len(bracket)+1):
            if bracket[:i].count(')') == bracket[:i].count('('):
                return ''.join(bracket[:i]), ''.join(bracket[i:]) if ''.join(bracket[i:])!="" else ""

    def isRight(bracket):
        stack = []
        for b in bracket:
            if stack and stack[-1] == '(' and b == ')':
                stack.pop()
            else:
                stack.append(b)
        return True if len(stack) == 0 else False

    def makingRight(u, v):
        res = ""
        res += "("
        res += subSolution(v)
        res += ")"
        for b in u[1:-1]:
            if b == "(":
                res += ")"
            else:
                res += "("
        return res

    def subSolution(bracket):
        if bracket!= "":
            u, v = splitBalance(bracket)
            if isRight(u):
                return u + subSolution(v)
            else:
                return makingRight(u, v)
        else:
            return ""

    return subSolution(p)