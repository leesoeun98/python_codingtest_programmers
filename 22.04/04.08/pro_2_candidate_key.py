"""
30분 소요, 예전 코드 봄
핵심 포인트
1. 최소성을 구하기
=> 각 attr 조합을 str permutation으로 만들고, candidate의 key도 str로 만들기
=> candidate key가 attr조합내에 있으면 최소성 아님 (순서 주의)
"""
from itertools import combinations, permutations


def solution(relation):
    col, candidate = len(relation[0]), []
    for i in range(1, col + 1):
        for attrs in list(combinations(range(col), i)):
            temp = set()
            for row in relation:
                temp.add(''.join([row[attr] for attr in attrs]))
            if len(temp) == len(relation):
                isMin = True
                attr_lst = [str(item) for item in attrs]
                attr_str_list = [''.join(item) for item in list(permutations(attr_lst, len(attr_lst)))]
                for candi in candidate:
                    candi_str = ''.join(candi)
                    for attr_str in attr_str_list:
                        if candi_str in attr_str:
                            isMin = False
                            break
                if isMin:
                    candidate.append(attr_lst)
    return len(candidate)



