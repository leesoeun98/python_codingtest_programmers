"""
5분 소요, 스스로 풂, bfs는 deque 이용
"""
from collections import deque
def solution(maps):
    n, m = len(maps) , len(maps[0])
    distance=[[0]*m for _ in range(n)]
    xd=[-1,1,0,0]
    yd=[0,0,-1,1]
    deq= deque()
    deq.append([0,0])
    distance[0][0]=1
    while deq:
        cur = deq.popleft()
        for i in range(4):
            x, y= xd[i]+cur[0], yd[i]+cur[1]
            if 0<=x<n and 0<=y<m and maps[x][y]==1:
                maps[x][y]=0
                distance[x][y]=distance[cur[0]][cur[1]]+1
                deq.append([x, y])
    return -1 if distance[n-1][m-1]==0 else distance[n-1][m-1]

