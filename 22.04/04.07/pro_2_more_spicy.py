"""
7분소요, 스스로 풂
핵심 포인트
1. 최소로 항상 정렬해야 하므로 최소 힙 쓰기
2. 문제 조건 잘 읽기 (가장 작은 원소가 k이상되면 바로 종료임)
"""
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    while scoville:
        if scoville[0]>=K:
            return count
        if len(scoville)>1:
            heapq.heappush(scoville, heapq.heappop(scoville)+2*heapq.heappop(scoville))
            count+=1
        else:
            if scoville[0]>=K:
                return count
            else:
                return -1
