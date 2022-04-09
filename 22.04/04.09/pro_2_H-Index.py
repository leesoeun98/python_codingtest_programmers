"""
3분 소요, 스스로 풂
핵심 포인트
1. 각 i번==h로 i번 이상 인용된 논문이 i편 이상인지만 확인
2. 어차피 큰게 답이니 거꾸로 i 가서 가장 먼저 조건 만족하면 바로 return
"""
def solution(citations):
    for i in range(len(citations), -1, -1):
        if len(list(filter(lambda x:x>=i, citations)))>=i:
            return i