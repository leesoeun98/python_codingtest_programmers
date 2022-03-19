"""
6분 소요, 스스로 풂
<핵심 포인트>
1. scoville을 최소힙을 이용해서 매번 sorting해주는게 중요
2. scoville의 두번째 요소도 뺄때는 len이 1이상이면 됨 (2이상x)
"""
import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count=0
    while scoville:
        first = heapq.heappop(scoville)
        if first>=K:
            return count
        else:
            if len(scoville)>=1:
                second = heapq.heappop(scoville)
                heapq.heappush(scoville, first+second*2)
                count+=1
            else:
                return -1

