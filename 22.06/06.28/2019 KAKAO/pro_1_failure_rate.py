"""
4분 소요, 스스로 풂
핵심 포인트
1. 문제 이해하기: 실패율 구하는 부분
2. dict sort 및 list comprehension
"""


def solution(N, stages):
    fail, total = {}, len(stages)

    for i in range(1, N + 1):
        cnt = stages.count(i)
        fail[i] = 0 if cnt == 0 else cnt / total
        total -= cnt
    fail = dict(sorted(fail.items(), key=lambda x: (-x[1], x[0])))

    return [key for key, value in fail.items()]