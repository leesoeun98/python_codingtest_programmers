"""
4분 소요, 스스로 풂
핵심 포인트
1. develope계산에 올림 들어감
2. duration이라는 변수를 둬서, 실제로 배포하는 것처럼 시물레이션 구현
=> duration보다 day가 크면 release하기, 아니면 count증가
"""
import math


def solution(progresses, speeds):
    develope, release, count= [], [], 0
    for progress, speed in zip(progresses, speeds):
        develope.append(math.ceil((100-progress)/speed))
    duration = develope[0]
    for day in develope:
        if duration<day:
            release.append(count)
            count=1
            duration = day
        else:
            count+=1
    release.append(count)
    return release
