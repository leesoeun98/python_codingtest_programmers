"""
1분 소요, 스스로 풂
핵심 포인트
1. zip 쓰기
"""
def solution(a, b):
    return sum([aa*bb for aa, bb in zip(a, b)])