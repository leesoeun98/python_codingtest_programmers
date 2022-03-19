"""
10분 소요, 스스로 풀었음
<핵심 포인트>
1. duration변수를 둬서 lst[i]랑 비교, duration이 더 크면 lst[i] 모두 같은날 배포 가능
2. duration이 더 작으면 배포하고 duration 갱신
"""
import math


def solution(progresses, speeds):
    lst=[]
    for progress, speed in zip(progresses, speeds):
        lst.append(math.ceil((100-progress)/speed))
    release=[]
    count, duration=0, lst[0]
    for i in range(len(lst)):
        if duration<lst[i]:
            release.append(count)
            count=1
            duration=lst[i]
        else:
            count+=1
    release.append(count)
    return release