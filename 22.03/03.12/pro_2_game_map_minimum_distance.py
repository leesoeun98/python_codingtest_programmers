"""
전형적 bfs 문제
예전에 풀었던 유사한 문제 답안 참고함
1. bfs -> deque 사용
2. distance 배열 만들기
3. while deq동안 deq의 첫 원소를 빼서 x, y 4방향을 탐색.
4. maps[x][y]가 갈 수 있는 곳이고, maps범위내에 있으면
5. maps[x][y]는 이제 갈 수 없는 곳으로 바꾸고, distance에 +1, deque에 x, y 추가
* x와 y가 m-1, n-1임을 헷갈리지 말기
"""
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(maps):
    deq= deque()
    deq.append([0,0])
    n, m = len(maps[0]), len(maps)
    distance=[[0]*n for _ in range(m)]
    maps[0][0], distance[0][0]=0, 1
    while deq:
        cur = deq.popleft()
        for i in range(4):
            x = cur[0]+dx[i]
            y = cur[1]+dy[i]
            if 0<=x<=m-1 and 0<=y<=n-1 and maps[x][y]==1:
                maps[x][y]=0
                distance[x][y]=distance[cur[0]][cur[1]]+1
                deq.append([x, y])
    return -1 if distance[m-1][n-1]==0 else distance[m-1][n-1]



