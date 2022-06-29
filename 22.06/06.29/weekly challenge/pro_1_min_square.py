"""
11분 소요, 스스로 풂
핵심 포인트
1. 문제 이해 - 한쪽은 min, 한쪽은 max로 정렬
"""


def solution(sizes):
    return max([max(a,b) for a, b in sizes])*max([min(a, b) for a, b in sizes])