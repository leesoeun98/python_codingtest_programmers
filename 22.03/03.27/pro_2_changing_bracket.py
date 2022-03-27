"""
23분 소요, 이전 코드 봄 (change, makingRight 부분에서)
재귀에 주의..뭘 return 하는지 명확히 알아야 하고 단계별 구현력도 높여야 함 + return 위치 주의
"""
def solution(p):
    def splitBalance(bracket):
        for i in range(1, len(bracket)+1):
            if bracket[:i].count('(') == bracket[:i].count(')'):
                return ''.join(bracket[:i]), ''.join(bracket[i:])

    def isRight(bracket):
        stack = []
        for b in bracket:
            if len(stack) and b == ')' and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(b)
        return True if len(stack) == 0 else False

    def reverseBracket(bracket):
        str = ""
        for b in bracket:
            if b == ')':
                str += '('
            else:
                str += ')'
        return str

    def makingRight(u, v):
        temp = '('
        temp += v
        temp += ')'
        temp += reverseBracket(u[1:-1])
        return temp

    def change(bracket):
        if isRight(bracket):
            return bracket
        u, v = splitBalance(bracket)
        if (isRight(u)):
            return u + change(v)
        else:
            return makingRight(u, change(v))
    return change(p)
