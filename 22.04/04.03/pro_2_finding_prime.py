"""
5부 소요, 스스로 풂
핵심 포인트
1. 소수인지 판단은 에라토스테네스 체 이용해서 한번만, 전역변수로
2. numbers로 순서 있게 숫자 나열해야 하므로 permutation이용
3. int로 변환해서, set에 저장
"""
isPrime=[False, False]+[True]*10**7
for i in range(2, len(isPrime)):
    if isPrime[i]:
        for j in range(i+i, len(isPrime), i):
            isPrime[j]=False

from itertools import permutations
def solution(numbers):
    candidate=set()
    count=0
    for i in range(1, len(numbers)+1):
        for perm in list(permutations(numbers, i)):
            candidate.add(int(''.join(perm)))
    for c in candidate:
        if isPrime[c]:
            count+=1
    return count