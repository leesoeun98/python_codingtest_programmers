"""
23분 소요, 스스로 풂
1. 유일성은 set 길이로 판단
2. 최소성은 issubset 이용
=> flag 두기, issubset 대상에 주의
"""
from itertools import combinations


def solution(relation):
    lst = []
    for i in range(1, len(relation) + 1):
        for combi_lst in list(combinations(range(len(relation[0])), i)):
            # 유일성
            sub = set()
            for row in relation:
                sub.add(''.join([row[col] for col in combi_lst]))
                if len(sub) == len(relation):
                    if len(lst)==0:
                        lst.append(set(combi_lst))
                    # 최소성
                    flag = True
                    for item in lst:
                        if item.issubset(set(combi_lst)):
                            flag = False
                    if flag:
                        lst.append(set(combi_lst))
    return len(lst)