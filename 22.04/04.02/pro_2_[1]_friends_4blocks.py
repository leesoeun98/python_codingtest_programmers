"""
3시간 40분 소요, dropBoard 부분만 참고
핵심 포인트
1. 각 함수별 return, 변수 이름 재대로
2. checkSame: bfs로 근처에 있는 애들 모두 같은 type으로 바꾸기
3. remove: 2*2 사각형 모양으로 봤을 때, 모두 같은 type이면, count가 4 이상이면 모두 remove (-1로 세팅)
4. drop: row만 swap
5. oneCycle: board_c랑 visited 매번 갱신, isAllBase 주의 + 각 type에 대해 지울 수 있으면 remove, remove할 거 없으면 False return (단, type별로 remove 판단해야 함, indent 위치 주의+type별로 -1을 -100으로 갱신)
=> -1이랑 -100 갱신 주의해야 하는거가 7개, 8개 remove 할 경우 같은 type이면 -1일때 해야 하는건데, type 하나 끝나면 바로 -100으로 해야 다른  type에서의 중복 remove없어짐
"""
x = [-1, 1, 0, 0]
y = [0, 0, -1, 1]
from collections import deque
def solution(m, n, board):
    def checkSame(start, temp_board, return_visited, tt):
        deq = deque([])
        deq.append(start)
        return_visited[start[0]][start[1]] = tt
        while deq:
            cur = deq.popleft()
            for i in range(4):
                xd, yd = x[i] + cur[0], y[i] + cur[1]
                if 0 <= xd < m and 0 <= yd < n and return_visited[xd][yd] != tt and temp_board[cur[0]][cur[1]] == temp_board[xd][yd]:
                    return_visited[xd][yd] = tt
                    deq.append([xd, yd])
        return return_visited
    def remove(t, m, n, visited, location, isRemoved):
        c=0
        for row in range(2):
            for col in range(2):
                if 0 <= location[0] + row < m and 0 <= location[1] + col < n:
                    if visited[location[0]+row][location[1]+col]==t or visited[location[0]+row][location[1]+col]==-1:
                        c+=1
        if c==4:
            for row in range(2):
                for col in range(2):
                    if 0<=location[0] + row<m and 0<=location[1] + col<n:
                        visited[location[0] + row][location[1] + col]=-1
                        isRemoved = True
        return isRemoved, visited

    def dropBoard(m, n, board_c):
        for row in range(m):
            for i in range(m-1):
                for j in range(n):
                    if board_c[i+1][j]=="":
                        board_c[i+1][j], board_c[i][j] = board_c[i][j], ""
        return board_c

    def oneCycle(m, n, board_c):
        visited = [[0] * n for _ in range(m)]
        isAllBase = False
        flag = False
        for i in range(m):
            for j in range(n):
                if board_c[i][j]=="":
                    visited[i][j]=-100
        tt = 1
        for i in range(m):
            for j in range(n):
                if visited[i][j]!=-100:
                    return_visited = checkSame([i, j], board_c, visited, tt)
                    isAllBase=True
                    tt += 1
        if isAllBase:
            visited = return_visited
            types = list(set((item for row in visited for item in row if item!=-100)))
            for t in types:
                if sum(row.count(t) for row in visited) >= 4:
                    candidates = [[index1, index2] for index1, value1 in enumerate(visited) for index2, value2 in
                                  enumerate(value1) if value2 == t]
                    for location in candidates:
                        isRemoved, return_visited2 = remove(t, m, n, visited,location, False)
                        if isRemoved:
                            flag = True
                            visited = return_visited2
                for i in range(m):
                    for j in range(n):
                        if visited[i][j] == -1:
                            board_c[i][j] = ""
                            visited[i][j] = -100
            if not flag:
                return False
            else:
                nonlocal board_copy
                board_copy = dropBoard(m, n, board_c)
                return True
        else:
            return False

    board_copy = [[[item] for item in row] for row in board]
    while True:
        flag = oneCycle(m, n, board_copy)
        if not flag:
            return len([[index1, index2] for index1, value1 in enumerate(board_copy) for index2, value2 in
                              enumerate(value1) if value2 == ""])

