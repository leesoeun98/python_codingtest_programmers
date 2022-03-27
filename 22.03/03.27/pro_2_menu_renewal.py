"""
33분 소요, 스스로 풂
문제 잘 읽기 (최소 2번이상 주문된, "최대"주문 된 조합을 고르는 거임 ㅠㅠ
핵심 포인트
1. order별로 course 길이 만큼 다 잘라서 default dict에 key로 넣기 (단, 알파벳 정렬 상태에서 해야함)
=> 이렇게 하면 course길이 별로 사람들이 몇번 주문했는지 횟수 알 수 있음
2. filter로 max이면서 2이상인 애들 뽑아서 저장
"""
import operator
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    ans = []
    for num in course:
        temp = defaultdict(int)
        for order in orders:
            for combi in [list(item) for item in combinations(order, num)]:
                temp[''.join(sorted(combi))] += 1
        for item in list(filter(lambda item: item[1]>=2 and item[1]>=max(temp.values()), dict(sorted(temp.items(), key=operator.itemgetter(1))).items())):
            ans.append(item[0])
    return sorted(ans)
