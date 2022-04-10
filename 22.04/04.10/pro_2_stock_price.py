"""
5분 소요, 스스로 풂
1. 각 i번쨰 item을 i+1~끝까지 비교
2. duration+=1은 항상 하다가 조건에 안맞으면 break로 중단
"""
def solution(prices):
    res=[]
    for i in range(len(prices)):
        duration=0
        for j in range(i+1, len(prices)):
            duration+=1
            if prices[i]>prices[j]:
                break
        res.append(duration)
    return res