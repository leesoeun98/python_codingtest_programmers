"""
1분 소요, 스스로 풂
dict쓰기
"""
def solution(absolutes, signs):
    dic={True:1, False:-1}
    return sum([a*dic[s] for a, s in zip(absolutes, signs)])