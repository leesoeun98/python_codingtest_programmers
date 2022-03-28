"""
7분 소요, 스스로 풂
핵심 포인트
1. 지수를 항상 최소 순으로 정렬해야 함 => 최소 힙, heapq 쓰기
2. while 종료, 조건 잘 지정하기
"""
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    while scoville:
        if scoville[0]>=K:
            return count
        elif len(scoville)==1 and scoville[0]<K:
            return -1
        elif len(scoville)>=2:
            f = heapq.heappop(scoville)
            s = heapq.heappop(scoville)
            heapq.heappush(scoville, f+s*2)
            count+=1
