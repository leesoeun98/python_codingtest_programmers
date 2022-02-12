"""
항상 최소값 순, 최대값 순으로 정렬이 필요하다면 => heapq
"""
import heapq
def solution(scoville, k):
    heapq.heapify(scoville)
    count=0
    while scoville:
        if scoville[0]>k:
            return count
        else:
            if len(scoville)>=2:
                heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
                count+=1
            else:
                return -1
