from itertools import combinations


def solution(nums):
    isprime = [False, False] + [True] * (sum(nums) - 1)
    for i in range(1, sum(nums) + 1):
        if isprime[i]:
            for j in range(i + i, sum(nums) + 1, i):
                isprime[j] = False
    ans = 0
    for num in list(set(combinations(nums, 3))):
        if isprime[sum(num)]:
            ans += 1
    return ans
