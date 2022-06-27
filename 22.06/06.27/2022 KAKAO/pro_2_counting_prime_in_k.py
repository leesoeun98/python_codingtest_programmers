"""
18분 소요, 스스로 풂
핵심 포인트
1. 진법 변환시 수가 너무 커질 수 있으므로 미리 소수 구하지 않고 그때마다 소수 판별해야 함
2. 10->k 진법은 직접해야 함
"""
import math


def solution(n, k):
    def isPrime(num):
        if num == 0 or num == 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    res, cnt = "", 0
    # 10진법 -> k진법
    while n > 0:
        res += str(n % k)
        n //= k
    lst = res[::-1].split('0')
    # 소수 판별
    for candi in lst:
        if candi != '' and isPrime(int(candi)):
            cnt += 1
    return cnt