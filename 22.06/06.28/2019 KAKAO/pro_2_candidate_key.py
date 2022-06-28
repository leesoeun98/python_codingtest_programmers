"""
15분 소요, 이전 코드 봄
핵심 포인트
1. 유일성 -> set, join, list comprehension 이용
2. 최소성 -> candidate의 모든 item에 대해 subset이 아니어야 하므로 flag 이용
"""
from itertools import combinations


def solution(relation):
    candidate, n = [], len(relation)

    for i in range(1, len(relation) + 1):
        for lst in list(combinations(range(len(relation[0])), i)):
            # 유일성
            if len(set([''.join([row[col] for col in lst]) for row in relation])) == n:
                # 최소성
                if len(candidate) == 0:
                    candidate.append(set(lst))
                flag = True
                for item in candidate:
                    if item.issubset(lst):
                        flag = False
                if flag:
                    candidate.append(set(lst))
    return len(candidate)

