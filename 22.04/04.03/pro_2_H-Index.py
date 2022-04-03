"""
5분 소요, 스스로 풂
핵심 포인트
1. h번 이상 인용된 논문 수만 비교하면 됨 (나머지는 조건 딱히 없으므로)
2. ans를 min값으로 초기화 후 max로 찾음 (list 원소가 1000개라 다 돌아도 됨)
"""
def solution(citations):
    #i가 곧 h
    ans=-1
    for i in range(len(citations)+1):
        if len(list(filter(lambda x:x>=i, citations)))>=i:
            ans = max(ans,i)
    return ans