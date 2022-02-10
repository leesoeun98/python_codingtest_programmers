def solution(lottos, win_nums):
    mincount=0
    for lotto in lottos:
        if lotto in win_nums:
            mincount+=1
    w = 7-(mincount+lottos.count(0)) if mincount+lottos.count(0)>1 else 6
    f = 7-mincount if mincount>1 else 6
    return [w,f]
