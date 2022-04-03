"""
6분 소요, 스스로 풂
핵심 포인트
1. 최소 거리를 구하라면 bfs
2. xd, yd 4방향 두고, distance 배열 만들어서 거리 갱신, visit여부는 map을 벽으로 막는걸로
3. deq에 넣는거 잊지 말기, while deq 동안 반복하기
4. row, col 헷갈리지 말기 + row, col 다를 수 있음에 주의하기
"""
xd=[-1,1,0,0]
yd=[0,0,1,-1]
from collections import deque
def solution(maps):
    col, row= len(maps[0]), len(maps)
    distance = [[0]*col for _ in range(row)]
    deq = deque([])
    deq.append([0,0])
    distance[0][0]=1
    while deq:
        cur = deq.popleft()
        for i in range(4):
            x, y = xd[i]+cur[0], yd[i]+cur[1]
            if 0<=x<row and 0<=y<col and maps[x][y]==1:
                maps[x][y]=0
                distance[x][y]=distance[cur[0]][cur[1]]+1
                deq.append([x, y])
    return distance[row-1][col-1] if distance[row-1][col-1]!=0 else -1



