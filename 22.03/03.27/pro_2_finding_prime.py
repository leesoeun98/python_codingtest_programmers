"""
25분 소요, 예전 코드 봄 (소수 구하는 부분)
핵심 포인트
1. 10**7 이상이면 런타임 에러가 나나봄..
2. 에라토스테네스 체 이용해서 prime 구하는거 외우기 ㅠㅠ
3. permutation으로 순서에 맞게 숫자 조합 구해서 int로 변환후 set에 add 
"""
from itertools import permutations

prime =[True] * (10**7)
prime[0], prime[1] = False, False
for i in range(len(prime)):
    if prime[i]:
        for j in range(i + i, len(prime), i):
            prime[j] = False

def solution(numbers):
    candidate=set()
    count=0
    for i in range(1, len(numbers)+1):
        for item in list(set(permutations(numbers, i))):
            candidate.add(int(''.join(item)))

    for candi in candidate:
        if prime[candi]:
            count+=1
    return count

