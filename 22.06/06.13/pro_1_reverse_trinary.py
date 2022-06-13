"""
5분 소요, 스스로 풂
핵심 포인트
1. 수학..계산..
"""


def solution(n):
    res, ans = "", 0
    while n > 0:
        res += str(n % 3)
        n //= 3
    for idx, num in enumerate(res[::-1]):
        ans += int(num) * (3 ** idx)
    return ans
