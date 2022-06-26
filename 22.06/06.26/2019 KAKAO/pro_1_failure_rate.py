"""
4분 소요, 스스로 풂
핵심 포인트
1. fail, total 갱신하기 (단, total이 0보다 작은지 확인)
2. sort 및 list comprehension
"""
def solution(N, stages):
    res, total=[], len(stages)
    for i in range(1, N+1):
        fail = stages.count(i)
        res.append([i, fail/total] if total>0 else [i, 0])
        total-=fail
    res.sort(key=lambda x:(x[1], -x[0]), reverse=True)
    return [stage for stage, failure in res]