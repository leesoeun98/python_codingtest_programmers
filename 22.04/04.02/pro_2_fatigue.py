"""
12분 소요, 스스로 풂
핵심 포인트
1. 어차피 8!까지이므로 permutation 사용해도 무방
2. k 직접 쓰지 않고 cur이라는 변수에 넣어서 써야함
"""
from itertools import permutations
def solution(k, dungeons):
    res=[]
    for perm in list(permutations(dungeons, len(dungeons))):
        count=0
        cur = k
        for dungeon in perm:
            if cur>=dungeon[0]:
                count+=1
                cur-=dungeon[1]
        res.append(count)
    return max(res)

