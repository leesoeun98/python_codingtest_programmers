"""
12분 소요, 스스로 풂
핵심 포인트
1. order별로 combinations 해서 dict에 count
2. dict 정렬 후 조건에 맞게 2개이상, max 값인 애들만 res에 append
"""
from itertools import combinations
def solution(orders, course):
    res=[]
    for cnt in course:
        dic={}
        for order in orders:
            for combi_list in list(combinations(order, cnt)):
                if ''.join(sorted(combi_list)) not in dic:
                    dic[''.join(sorted(combi_list))]=0
                dic[''.join(sorted(combi_list))]+=1
        sorted_dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
        for key, value in sorted_dic.items():
            if value==max(sorted_dic.values()) and value>=2:
                res.append(key)
    return sorted(res)