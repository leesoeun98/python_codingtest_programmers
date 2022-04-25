"""
40분 소요, 예전 코드 봄
틀린 부분
1. list에서 item의 최소성을 만족하지 못함 
"""
from itertools import combinations, permutations


def solution(relation):
    candidate = []
    for i in range(1, len(relation[0])+1):
        for lst in combinations(range(len(relation[0])), i):
            attrs = set(''.join([row[idx] for idx in lst]) for row in relation)
            if len(attrs) == len(relation):
                isMin = True
                idx_list = [str(item) for item in lst]
                idx_permu_list = [''.join(item) for item in list(permutations(idx_list, len(idx_list)))]
                for key in candidate:
                    key_str = ''.join(key)
                    for idx_permu in idx_permu_list:
                        if key_str in idx_permu:
                            isMin=False
                            break
                if isMin:
                    candidate.append(idx_list)
    return candidate


print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
