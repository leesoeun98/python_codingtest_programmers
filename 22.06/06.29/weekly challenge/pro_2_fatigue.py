"""
8분 소요, 스스로 풂
핵심 포인트
1. 개수 몇개 안되니 permutaion으로 큰 값부터 확인, 만족 시 바로 return으로 시간 절약
"""
from itertools import permutations


def solution(k, dungeons):
    for i in range(len(dungeons), -1, -1):
        for lst in list(permutations(dungeons, i)):
            kc, flag =k, True
            for item in lst:
                if kc<item[0]:
                    flag = False
                    break
                kc-=item[1]
            if flag:
                return i