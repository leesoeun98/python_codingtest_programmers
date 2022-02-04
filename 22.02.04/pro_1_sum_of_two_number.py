"""
수열의 합 = n(첫항+마지막항)/2
"""
def solution(a, b):
    return (abs(a-b)+1)*(a+b)/2
"""
def solution(a, b):
    return sum(list(i for i in range(min(a, b), max(a, b)+1)))
"""