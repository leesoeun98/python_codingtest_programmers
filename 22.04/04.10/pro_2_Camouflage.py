"""
3분 소요, 스스로 풂
핵심 포인트
1. dic에 type별로 옷 저장
2. dic[key]의 len+1 (착장 안한 경우도 포함해야 함)
3. count-1 (모두 착용 안한 경우 -1)
"""
def solution(clothes):
    dic, count={}, 1
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]] = []
        dic[cloth[1]].append(cloth[0])
    for key in dic.keys():
        count*=(len(dic[key])+1)
    return count-1