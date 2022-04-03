"""
6분 소요, 스스로 풂
핵심 포인트
1. type 별로 clothe를 dict에 append
2. 경우의 수 구할 때 안입는 경우도 포함 위해 +1 해서 곱하고, 맨 마지막에 아무것도 안입는 경우 제외위해 -1
"""
def solution(clothes):
    dic={}
    for cloth in clothes:
        if cloth[1] not in dic:
            dic[cloth[1]]=[]
        dic[cloth[1]].append(cloth[0])
    ans=1
    for key in dic:
        # 안 입는 경우 포함 위해 +1
        ans*=(len(dic[key])+1)
    #단, 아무것도 안입는 경우는 제외
    return ans-1