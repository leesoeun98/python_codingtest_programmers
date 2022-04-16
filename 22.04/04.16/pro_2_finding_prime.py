"""
7분 소요, 스스로 풂
핵심 포인트
1. permutation으로 조합 모두 구하기
2. isPrime은 조합의 최대값으로 (시간 초과 안나게)
3. res 값 모두 순회해서 prime이면 count+=1
"""
from itertools import permutations
def solution(numbers):
    res, count=set(), 0
    for length in range(1, len(numbers)+1):
        for lst in permutations(numbers, length):
            res.add(int(''.join(map(str, lst))))
    isPrime = [False, False] + [True] * max(map(int, list(res)))
    for i in range(2, len(isPrime)):
        if isPrime:
            for j in range(2 * i, len(isPrime), i):
                isPrime[j] = False
    for r in res:
        if isPrime[r]:
            count+=1
    return count