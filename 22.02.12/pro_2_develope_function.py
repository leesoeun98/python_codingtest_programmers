"""
예제 이해 잘하기 => 반올림 문제 
"""
import math
def solution(progresses, speeds):
    working, deploy=[], []
    for progress, speed in zip(progresses,speeds):
        working.append(math.ceil((100-progress)/speed))
    cur, count=working[0], 0
    while working:
        if cur>=working[0]:
            count+=1
        else:
            deploy.append(count)
            cur=working[0]
            count=1
        working.pop(0)
    deploy.append(count)
    return deploy