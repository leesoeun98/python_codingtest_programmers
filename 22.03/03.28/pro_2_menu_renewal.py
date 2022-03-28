"""
8분 소요, 스스로 풂
핵심 포인트
1. 문제이해: 최대 횟수이면서 2이상인 조합만 뽑기
2. 각 order별로 count길이 만큼 dict의 key로 삼아서 언급 횟수 세기
3. dict에 filter써서 list 생성
"""
from itertools import combinations
def solution(orders, course):
    ans=[]
    for count in course:
        dic={}
        for order in orders:
            for item in list(set(combinations(order, count))):
                combi = ''.join(sorted(item))
                if combi in dic.keys():
                    dic[combi]+=1
                else:
                    dic[combi]=1
        res = dict(filter(lambda x:x[1]>=max(dic.values()) and x[1]>=2, dic.items())).keys()
        for item in res:
            ans.append(item)
    return sorted(ans)

