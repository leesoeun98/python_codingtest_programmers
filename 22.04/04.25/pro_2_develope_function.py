"""
8분 소요, 스스로 풂 (그러나 테케 공유받음)
틀린 부분
1. float로 형변환 안한 거
2. today for문 내에서 갱신 안한 것
"""
import math

def solution(progresses, speeds):
    develop=[math.ceil((100-progress) / float(speed)) for progress, speed in zip(progresses, speeds)]
    today, release, count=develop[0], [], 1
    for i in range(1, len(develop)):
        if today>=develop[i]:
            count+=1
        else:
            release.append(count)
            today = develop[i]
            count=1
    release.append(count)
    return release
