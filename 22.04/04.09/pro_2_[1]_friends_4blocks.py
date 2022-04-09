"""
1시간 반 소요, 예전 코드 봄
핵심 포인트
1. 변수들 범위, 갱신에 주의 특히 nonlocal로 쓸거면 해당 변수 계속 갱신해줘야 무한 루프 안탐 // board_copy = dropBoard(board_c)
2. 각 함수들 구현 (변수로 characterT, board_c 이런거 넘기기에 주의)
3. while문 도임
4. 시간 복잡도 줄이기 위해 이중 for문이면 if sum(row.count(c) for row in characterType) >= 4: 조건 추가하기
"""
from collections import deque
def solution(m, n, board):
    total_count = 0
    xd=[-1,1,0,0]
    yd=[0,0,-1,1]

    # bfs로 주변에 같은거 다 type같은걸로 변형하는 함수
    def checkSame(i, j, ctype, board_c,visited, characterT):
        nonlocal xd, yd, m, n
        deq = deque()
        deq.append([i, j])
        visited[i][j] = True
        characterT[i][j] = ctype
        while deq:
            cur = deq.popleft()
            for i in range(4):
                x, y = xd[i] + cur[0], yd[i] + cur[1]
                if 0 <= x < m and 0 <= y < n:
                    if not visited[x][y] and board_c[x][y]==board_c[cur[0]][cur[1]]:
                        visited[x][y] = True
                        characterT[x][y] = ctype
                        deq.append([x, y])
        return characterT
    #2*2 사각형으로 pop
    def checkSquare(x, y, c, characterT):
        count=0
        nonlocal m, n
        for i in range(2):
            for j in range(2):
                curx, cury = x+i, y+j
                if 0<=curx<m and 0<=cury<n:
                    if characterT[curx][cury]==c or characterT[curx][cury]==0:
                        count+=1
        if count==4:
            for i in range(2):
                for j in range(2):
                    curx, cury = x + i, y + j
                    characterT[curx][cury]=0
            return True
        return False
    #characterType이 -1이면 모두 내리기
    def dropBoard(board_c):
        nonlocal m, n
        for row in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board_c[i+1][j]=="":
                        board_c[i][j], board_c[i+1][j]=board_c[i+1][j], board_c[i][j]
        return board_c

    def oneCycle(board_c):
        nonlocal m, n, total_count, board_copy
        visited = [[False] * n for _ in range(m)]
        characterType = [[-1] * n for _ in range(m)]
        ctype, ctypes, flag=1, set(), False

        for i in range(m):
            for j in range(n):
                if not visited[i][j] and board_c[i][j]!="":
                    characterType = checkSame(i, j, ctype, board_c, visited, characterType)
                    ctype+=1

        for i in range(m):
            for j in range(n):
                ctypes.add(characterType[i][j])
        if -1 in ctypes:
            ctypes.remove(-1)

        for c in ctypes:
            if sum(row.count(c) for row in characterType) >= 4:
                for i in range(m):
                    for j in range(n):
                        if characterType[i][j]==c or characterType[i][j]==0:
                            if checkSquare(i, j, c, characterType):
                                flag = True
            for i in range(m):
                for j in range(n):
                    if characterType[i][j]==0:
                        characterType[i][j]=-1
                        board_c[i][j]=""
                        total_count+=1
        board_copy = dropBoard(board_c)

        return flag

    board_copy = [[item for item in row]for row in board]
    while True:
        if not oneCycle(board_copy):
            return total_count