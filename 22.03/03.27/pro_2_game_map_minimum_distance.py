"""
10분 소요, 스스로 풂
=> map에서 최소거리 구하라 하면 bfs, 갈 수 있는 거리 count 구하라 하면 dfs
핵심 포인트
1. n,m 이랑 x, y 구분 잘하기
2. deque에 넣고 while deque동안 하되, distance배열과 maps배열로 visited여부 확인하기, 거리는 distance 배열로 갱신
"""
from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    distance=[[0]*m for _ in range(n)]
    distance[0][0]=1
    xd=[-1,1,0,0]
    yd=[0,0,-1,1]
    deq = deque()
    deq.append([0,0])
    while deq:
        cur= deq.popleft()
        for i in range(4):
            x, y= cur[0]+xd[i], cur[1]+yd[i]
            if 0<=x<n and 0<=y<m and distance[x][y]==0 and maps[x][y]==1:
                distance[x][y]=distance[cur[0]][cur[1]]+1
                maps[x][y]=0
                deq.append([x, y])
    return distance[n-1][m-1] if distance[n-1][m-1]!=0 else -1