"""
6분 소요, 스스로 풂
핵심 포인트
1. {{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}} 이 문제 조건
2. 문자열 파싱하고 list comprehension 사용이 중요
"""
def solution(s):
    res = []
    s = s.rstrip('}}').lstrip('{{').split('},{')
    s = sorted(s, key=lambda x: x.count(','))
    nums = [[int(item) for item in items.split(',')] for items in s]
    for row in nums:
        for item in row:
            if item not in res:
                res.append(item)
    return res
