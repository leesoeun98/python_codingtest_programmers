"""
7분 소요, 예전 코드 봄
핵심 포인트
1. 어차피 던전 수 8개라 8!이 최대 =>permutation쓰자
2. perm 마다 count세서 res에 저장후 max값 return
"""
from itertools import permutations
def solution(k, dungeons):
    res=[]
    for perm in list(permutations(dungeons, len(dungeons))):
        copy_k, count = k, 0
        for dungeon in perm:
            if copy_k>=dungeon[0]:
                copy_k-=dungeon[1]
                count+=1
        res.append(count)
    return max(res)