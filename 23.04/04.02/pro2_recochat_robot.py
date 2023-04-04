# 1차 실패 - 1시간 3분 소요
# 2차 성공- 23분 소요 (다른 사람 풀이 보고 풂)
# bfs => 이미 갔던 방향이면 탐색 중단 + G면 bfs니까 바로 curDist return (여기까진 맞음)
# recursion 잘 못 쓰겠으면 얌전히 bfs는 queue, dfs는 stack쓰자
from collections import deque

directionX = [1, 0, -1, 0]
directionY = [0, -1, 0, 1]


def solution(board):
    distanceList = [[12345678] * len(board[0]) for _ in range(len(board))]
    queue = deque()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                queue.append([i, j, 0])
                distanceList[i][j] = 0
        if queue:
            break

    # bfs - queue
    while queue:
        curX, curY, curDist = queue.popleft()
        if board[curX][curY] == "G":
            return curDist

        # 4방향 탐색 => while로 각 방향마다 끝까지 이동
        for d in range(4):
            nextX, nextY = curX, curY

            while 0 <= nextX + directionX[d] < len(board) and 0 <= nextY + directionY[d] < len(board[0]) and \
                board[nextX + directionX[d]][nextY + directionY[d]] != "D":
                nextX += directionX[d]
                nextY += directionY[d]

            # nextX, nextY를 방문한 적 없고, 거리가 적으면 queue에 append & distanceList 갱신
            if distanceList[nextX][nextY] > curDist + 1:
                distanceList[nextX][nextY] = curDist + 1
                queue.append([nextX, nextY, distanceList[nextX][nextY]])
    return -1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))