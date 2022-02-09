"""
시간 초과 => 이중 for문 x
def solution(N, stages):
    res={}
    for i in range(1, N+1):
        reach=0
        clear=0
        for player in stages:
            if player>=i:
                reach+=1
            if player>i:
                clear+=1
        if reach==0:
            res[i]=0
        else:
            res[i]=clear/reach
    ans = sorted(res.items(), key = lambda item: item[1], reverse= True)
    return list(map(lambda x:x[0], ans))
"""
def solution(N, stages):
    res={}
    reach=len(stages)
    for i in range(1, N+1):
        clear = stages.count(i)
        if reach==0:
            res[i]=0
        else:
            res[i]=clear / reach
        reach-=clear
    return sorted(res, key=lambda x:res[x], reverse=True)