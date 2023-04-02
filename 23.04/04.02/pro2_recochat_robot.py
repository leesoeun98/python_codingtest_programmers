# 1차 실패 - 1시간 3분 소요
# 12: 57 - 1:05 (다른 사람 풀이 보는 중이나 아직 해결 못함)
# dfs / bfs => 내가 생각한 종료 조건 : 이미 갔던 방향이거나 / G면 종료 (여기까진 맞음)

directionX = [1, 0, -1, 0]
directionY = [0, -1, 0, 1]
answerList = []


def dfs(depth, directionIdx, curX, curY, board):
    if board[curX][curY] == "G":
        answerList.append(depth)
        return
    # 맨끝까지 이동
    while True:
        if curX + directionX[directionIdx] < 0 or curX + directionX[directionIdx] > len(board) - 1 or curY + directionY[directionIdx] < 0 or curY + directionY[directionIdx] > len(board[0]) - 1 or board[curX + directionX[directionIdx]][curY + directionY[directionIdx]] == "D":
            break
        curX += directionX[directionIdx]
        curY += directionY[directionIdx]
    if board[curX][curY] == "X":
        return

    board[curX][curY] = "X"
    dfs(depth + 1, 0, curX, curY, board)
    dfs(depth + 1, 1, curX, curY, board)
    dfs(depth + 1, 2, curX, curY, board)
    dfs(depth + 1, 3, curX, curY, board)


def solution(strBoard):
    startX, startY = 0, 0
    board = [['.']*len(strBoard[0]) for _ in range(len(strBoard))]

    for i in range(len(strBoard)):
        for j in range(len(strBoard[0])):
            if strBoard[i][j] == "R":
                startX, startY = i, j
            board[i][j] = strBoard[i][j]

    dfs(0, 0, startX, startY, board)
    dfs(0, 1, startX, startY, board)
    dfs(0, 2, startX, startY, board)
    dfs(0, 3, startX, startY, board)
    return min(answerList) - 1 if len(answerList) > 0 else - 1

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))