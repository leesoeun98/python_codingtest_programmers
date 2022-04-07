"""
12분 소요, 스스로 풂
핵심 포인트
1. 문제 이해 - dic 초기 값은 0이 아니라 1
2. dic filter 아직도 부족
3. 각 order마다 2, 3, 4등 문자 개수만큼 combination 뽑아내서 알파벳 순 정렬해서 dict로 저장하겠다가 핵심
"""
from itertools import combinations
def solution(orders, courses):
    result=[]
    for course in courses:
        dic={}
        for order in orders:
            for combi in list(combinations(order, course)):
                if ''.join(sorted(combi)) in dic:
                    dic[''.join(sorted(combi))]+=1
                else:
                    dic[''.join(sorted(combi))]=1
        res = dict(filter(lambda x:x[1]>=2 and x[1]==max(dic.values()), dic.items()))
        for key in res.keys():
            result.append(key)
    return sorted(result)

