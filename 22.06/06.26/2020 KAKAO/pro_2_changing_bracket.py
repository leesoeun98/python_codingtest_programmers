"""
16분 소요, 스스로 풂
핵심 포인트
1. 구현력, 재귀
2. 틀린 부분: split에서 len(bracket)+1을 해줘야 함 안그러면 ()같이 길이가 2이면 i가 1만 돼서 오류남
"""


def solution(p):
    def isRight(bracket):
        stack = []
        for b in bracket:
            if b == ')' and len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(b)
        return True if len(stack) == 0 else False

    def split(bracket):
        for i in range(1, len(bracket)+1):
            if bracket[:i].count('(') == bracket[:i].count(')'):
                u = ''.join(bracket[:i])
                v = "" if i == len(bracket) == 0 else ''.join(bracket[i:])
                print(u, v)
                return u, v

    def change(bracket):
        if bracket == "":
            return ""
        u, v = split(bracket)
        print(u, v)
        if isRight(u):
            return u + change(v)
        else:
            res = ""
            res += '('
            res += change(v)
            res += ')'
            for uu in u[1:-1]:
                if uu == '(':
                    res += ')'
                else:
                    res += '('
            return res

    return change(p)