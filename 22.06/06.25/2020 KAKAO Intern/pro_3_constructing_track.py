"""
43분 소요, 다른 사람 풀이 봄
핵심 포인트
1. bfs인건 알고 있었음
=> cost, direction 정보도 queue에 넣기
=> 4방향으로 cost 정보 다 저장하기
=> cost[d][x][y] 갱신
=> 마지막 까지 갔으면 continue로 해당 방향 탐색 중지
"""
from collections import deque
xd=[-1,1,0,0]
yd=[0,0,-1,1]


def solution(board):
    ans, n =int(1e9), len(board)
    cost=[[[int(1e9)]*n for _ in range(n)] for _ in range(4)]
    queue = deque()
    queue.append([0,0,0,1])
    queue.append([0,0,0,3])
    while queue:
        px, py, pco, pdi = queue.popleft()
        for d in range(4):
            x, y = px+xd[d], py+yd[d]
            if 0<=x<n and 0<=y<n and board[x][y]==0:
                cco = pco+1
                if pdi!=d:
                    cco+=5
                if cost[d][x][y]>cco:
                    cost[d][x][y] = cco
                    if y == n-1 and x == n-1:
                        continue
                    queue.append([x, y, cco, d])
    for i in range(4):
        ans = min(ans, cost[i][n-1][n-1])
    return ans*100