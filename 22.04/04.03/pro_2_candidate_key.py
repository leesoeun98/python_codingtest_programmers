"""
44분 소요, 스스로 풂
핵심 포인트
1. unique: 속성별로 다 join한 문자열 set이 relation tuple 개수랑 맞는지 확인
2. min: 이게 젤 오래 걸림.. key안에 있는 모든 value에 대해 combi가 갖고있으면 안됨
=> attrs=[''.join(map(str, items)) for items in list(permutations(combi, len(combi)))]
이렇게 combi에 대해 나올 수 있는 모든 순열을 구해서 문자열로 만듦
=> strk = ''.join(map(str, k))
이렇게 key에 대해 나올 수 있는 모든 문자열을 만듦
그래서 srtk가 각 attr에 있는지로 최소성 확인
"""
from itertools import combinations, permutations
def solution(relation):
    key=[]
    col = range(len(relation[0]))
    for i in range(1, len(col)+1):
        for combi in list(combinations(col, i)):
            temp=set()
            for tuple in relation:
                temp.add(''.join([tuple[attr] for attr in combi]))
            if len(temp)==len(relation):
                isMin = True
                attrs=[''.join(map(str, items)) for items in list(permutations(combi, len(combi)))]
                for k in key:
                    strk = ''.join(map(str, k))
                    for attr in attrs:
                        if strk in attr:
                            isMin = False
                if isMin:
                    key.append(list(combi))
    return len(key)


