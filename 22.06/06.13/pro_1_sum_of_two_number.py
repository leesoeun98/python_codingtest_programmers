"""
1분 소요, 스스로 풂
핵심 포인트
1. 100이하고 100C2가지는 몇개 안되니까 라이브러리 쓰자
"""
from itertools import combinations
def solution(numbers):
    res=set()
    for combi in list(combinations(numbers, 2)):
        res.add(sum(combi))
    return sorted(list(res))