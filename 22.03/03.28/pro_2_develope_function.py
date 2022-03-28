"""
5분 소요, 스스로 풂
핵심 포인트
1. day list 구할 때 list comprehension, math.ceil 쓰기
2. 배포날짜를 실제처럼 생각하기 (duration, count 변수를 두어서 duration, count 갱신하면서 day의 원소들 세기)
=> 연속되는 반복 단어 세는 방법과 유사
"""
import math


def solution(progresses, speeds):
    day = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses, speeds)]
    duration, count, release= day[0], 0, []
    for d in day:
        if d<=duration:
            count+=1
        else:
            release.append(count)
            duration=d
            count=1
    release.append(count)
    return release