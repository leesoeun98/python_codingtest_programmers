"""
16분 소요, 예전 코드 봄
핵심 포인트
1. 다익스트라 문제임 => dic으로 양방향 maps 정보 저장
2. distance 최소화 위해 heapq 사용
3. distance 갱신하기
=> 1부터 cur까지가 time인데, time보다 distance가 작으면 갱신할 필요 없음
4. 인접 node로 확장
=> dic[cur]의 next 모두 검토
=> distance 갱신하기 (1부터 cur까지 distance+cur부터 next time < 1부터 next까지 distance면 distance 갱신)
=> q에 해당 next 넣기 (단, 넣을때는 1부터 next까지 distance랑, next의 idx)
"""
import heapq
def solution(N, roads, K):
    dic, q, distance={}, [], [int(1e9)]*(N+1)
    for i in range(1, N+1):
        dic[i]=[]
    for road in roads:
        dic[road[0]].append([road[1], road[2]])
        dic[road[1]].append([road[0], road[2]])
    #q는 (time, index) list 로 time최소인 순으로 정렬됨
    heapq.heappush(q, [0,1])
    distance[1]=0
    while q:
        time, cur = heapq.heappop(q)
        #1번부터 cur까지 time 갱신
        if distance[cur]<time:
            continue
        for next in dic[cur]:
            #time 갱신 (1번부터 cur까지 time + cur부터 next까지 time이랑 1부터 next까지 time 비교)
            #dic은 idx, time순
            if distance[cur] + next[1]<distance[next[0]]:
                distance[next[0]]=distance[cur]+next[1]
                heapq.heappush(q, (distance[cur] + next[1], next[0]))
    return len(list(filter(lambda x:x<=K, distance)))
