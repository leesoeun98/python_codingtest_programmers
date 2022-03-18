"""
거리를 최소로 정렬하기 위해 heapq 사용
40분 정도 걸림, 다른 사람 풀이 봄 => 양방향임에 매우 주의
"""
import heapq
def solution(N, road, K):
    map = [[] for _ in range(N + 1)]
    # 시작점부터 각 index까지 거리
    distance = [int(1e9)] * (N + 1)
    # map 만들기 (양방향임에 주의)
    for start, end, time in road:
        map[start].append((end, time))
        map[end].append((start, time))
    q=[]
    #heapq에 dist, node 넣기
    heapq.heappush(q,(0,1))
    distance[1]=0
    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur]<dist:
            continue
        for next in map[cur]:
            #cost:1~cur+cur~next
            cost = distance[cur]+next[1]
            if cost<distance[next[0]]:
                distance[next[0]]=cost
                heapq.heappush(q, (cost, next[0]))
    return len([i for i in distance if i<=K])


