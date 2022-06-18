"""
10분 소요, 예전 코드 봄
핵심 포인트
1. 풀이를 모르겠고, 배열 길이가 8정도면 그냥 순열로 쫙 나얄 한 후 하나씩 다 계산하자 그래봤지 8! 이다
"""
from itertools import permutations


def solution(k, dungeons):
    cnt = []
    for perm in list(permutations(dungeons, len(dungeons))):
        count, k_copy = 0, k
        for threshold, using in perm:
            if k_copy >= threshold:
                count += 1
                k_copy -= using
        cnt.append(count)
    return max(cnt)
