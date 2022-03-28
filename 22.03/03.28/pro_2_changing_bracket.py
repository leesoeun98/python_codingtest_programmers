"""
15분 소요, 함수 구성에서 예전 코드 참고함 (change쪽)
핵심 포인트
1. 구현력, 재귀 이해
2. 제발제발 오타 내지 않기, 한 단계별로 맞는지 확인하기 (split에서 bracket[:i]인데 bracket으로 오타냄)
"""
def solution(p):
    def splitBracket(bracket):
        for i in range(1, len(bracket)+1):
            if bracket[:i].count('(')==bracket[:i].count(')'):
                return ''.join(bracket[:i]), ''.join(bracket[i:])
    def isRight(bracket):
        stack=[]
        for b in bracket:
            if stack and stack[-1]=='(' and b==')':
                stack.pop()
            else:
                stack.append(b)
        return True if len(stack)==0 else False
    def makingRight(u, v):
        temp=""
        temp+='('
        temp+=v
        temp+=')'
        for b in u[1:-1]:
            if b=='(':
                temp+=')'
            else:
                temp+='('
        return temp
    def changeBracket(bracket):
        if isRight(bracket):
            return bracket
        u, v = splitBracket(bracket)
        if isRight(u):
            return u+changeBracket(v)
        else:
            return makingRight(u, changeBracket(v))
    return changeBracket(p)
