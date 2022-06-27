"""
2분 소요, 스스로 풂
"""
from itertools import combinations


def solution(numbers):
    ans=set()
    for lst in list(combinations(numbers,2)):
        ans.add(sum(lst))
    return sorted(list(ans))