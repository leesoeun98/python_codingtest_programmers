"""
1분 소요, 스스로 풂
"""
def solution(absolutes, signs):
    return sum([a if s else -a for a, s in zip(absolutes, signs)])