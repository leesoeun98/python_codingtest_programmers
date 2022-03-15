"""
2시간 걸림...다른 사람 코드도 봄 (근데 분명 아이디어는 비슷했음)

1. combination 만들 때 index error 주의 len(relation[0])으로 해야 속성임
2. set 만들 때 tuple이어야 하는거 주의
3. 유일성이 충족된다면, if len(set(tables))==len(relation): 이걸로
4. 최소성도 충족해야함. candidate의 각 item인 list에 대해서 해당 item과 com이 서로 subset인지 확인
5. subset인 적이 없어야 최소성도 충족한 것이므로 candidate에 저장
"""
from itertools import combinations
def solution(relation):
    candidate = []
    for i in range(1, len(relation[0])+1):
        combi = combinations(range(len(relation[0])), i)
        for com in combi:
            tables = [tuple([item[index] for index in com]) for item in relation]
            if len(set(tables))==len(relation):
                flag = True
                for item in candidate:
                    if set(item).issubset(set(com)):
                        flag = False
                if flag:
                    candidate.append(com)
    return len(candidate)
