"""
5분 소요, 스스로 풂
핵심 포인트
1. prime을 에라토스테네스 체로
2. permutation으로 순서대로 숫자 나열해서 int로 변환 후 set에 저장
"""
isPrime=[False, False]+[True]*10**7
for i in range(2, len(isPrime)):
    if isPrime[i]:
        for j in range(2*i, len(isPrime), i):
            isPrime[j]=False

from itertools import permutations
def solution(numbers):
    nums, count= set(), 0
    for i in range(1, len(numbers)+1):
        for lst in permutations(numbers, i):
            nums.add(int(''.join(lst)))
    for n in nums:
        if isPrime[n]:
            count+=1
    return count
