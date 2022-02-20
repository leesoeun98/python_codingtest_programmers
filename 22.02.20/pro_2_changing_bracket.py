"""
1. 함수 안에 함수 만드는거 주의
2. 재귀호출 주의 (change 함수)
단계별로 수도코드처럼 쪼개서 구현하기
"""
def solution(p):
    def split(p):
        lst = []
        for bracket in p:
            lst.append(bracket)
            if lst.count('(') == lst.count(')'):
                break
        u = ''.join(lst)
        v = ''.join(p[len(lst):])
        return u, v

    def is_right(s):
        stack = []
        for bracket in s:
            if bracket == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
            else:
                stack.append(bracket)
        return False if len(stack) > 0 else True

    def making_right(u, v):
        str='('
        str+=v
        str+=')'
        lst=[]
        for bracket in u[1:-1]:
            if bracket=='(':
                lst.append(')')
            else:
                lst.append('(')
        str+=''.join(lst)
        return str

    def change(p):
        if is_right(p):
            return p
        u, v = split(p)
        if is_right(u):
            return u+change(v)
        else:
            return making_right(u,change(v))

    return ''.join(change(p))


