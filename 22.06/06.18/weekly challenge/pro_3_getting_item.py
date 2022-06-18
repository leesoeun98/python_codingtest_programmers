"""
58분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 말 그대로 구현하자 => 직사각형 두배로 해서 테두리는 1로, 내부는 0으로 만들자 (초기화르 0으로 해서 당연히 외부도 0)
2. 최소 거리=> bfs => bfs로 queue 이용 => 1이고, visit 안했으면 넣는걸로
"""

from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    cX, cY, iX, iY = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    board = [[0] * 101 for _ in range(101)]
    visit = [[0] * 101 for _ in range(101)]
    direction = [[0, 1], [-1, 0], [1, 0], [0, -1]]
    visit[cX][cY] = 1
    queue = deque()
    queue.append([cX, cY])

    # 사각형 칠하기 (테두리, 내부)
    for x1, y1, x2, y2 in rectangle:
        for row in range(2 * x1, 2 * x2 + 1):
            for col in range(2 * y1, 2 * y2 + 1):
                board[row][col] = 1

    # 사각형 칠하기 (내부를 0으로)
    for x1, y1, x2, y2 in rectangle:
        for row in range(2 * x1 + 1, 2 * x2):
            for col in range(2 * y1 + 1, 2 * y2):
                board[row][col] = 0

    while queue:
        x, y = queue.popleft()
        if x == iX and y == iY:
            return (board[x][y] - 1) // 2
        for dx, dy in direction:
            nextX, nextY = x+dx, y+dy
            if 0 <= nextX < 101 and 0 <= nextY < 101 and visit[nextX][nextY] == 0 and board[nextX][nextY] != 0:
                board[nextX][nextY] = board[x][y] + 1
                visit[nextX][nextY] = 1
                queue.append([nextX, nextY])
