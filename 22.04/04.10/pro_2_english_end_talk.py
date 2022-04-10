"""
21분 소요, 스스로 풂
핵심 포인트
1. (idx+1)%n 수식 주의, 아예 idx, person, round, word까지 다 저장해두고, stack으로 확인
3. list index접근에서 계속 실수함 주의하기
"""
def solution(n, words):
    wwords, stack=[], []
    round=1
    for idx, word in enumerate(words):
        wwords.append([idx, (idx+1)%n if(idx+1)%n!=0 else n , round, word])
        if (idx+1)%n==0:
            round+=1
    for idx, value in enumerate(words):
        if stack:
            if value in stack or value[0]!=stack[-1][-1]:
                lst = list(filter(lambda x:x[0]==idx, wwords))
                return [lst[0][1], lst[0][2]]
        stack.append(value)
    return [0,0]