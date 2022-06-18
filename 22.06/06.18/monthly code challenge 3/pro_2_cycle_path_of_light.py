"""
30분 소요, 다른 사람 코드 봄
핵심 포인트
1. grid[x][y][d] 3차원 배열 만들기
2. grid의 row, grid의 col, grid의 direction 으로 for문 돌리면서 simulate, 결과가 0 이 아니면 append
3. answer sort
4. simulate
=> S는 방향 그대로
=> L은 왼쪽으로 (d-1)%4 왜???
=> R은 오른쪽으로 (d+1)%4
=> while True일 동안 x, y, d 바꿔가는데 visited 한 곳이고 sx, sy, d랑 같으면 cnt return 아니면 0 return (중복되는 사이클이므로)
"""
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def solution(grid):
    n, m = len(grid), len(grid[0])
    answer = []
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]

    def simulate(sx, sy, sd, grid):
        nonlocal visited
        x, y, d = sx, sy, sd
        visited[x][y][d] = True
        cnt = 0
        while True:
            x = (x + dx[d]) % n
            y = (y + dy[d]) % m
            cnt += 1
            if grid[x][y] == 'L':
                d = (d - 1) % 4
            elif grid[x][y] == 'R':
                d = (d + 1) % 4
            if visited[x][y][d]:
                if (x, y, d) == (sx, sy, sd):
                    return cnt
                else:
                    return 0
            visited[x][y][d] = True

    for sx in range(n):
        for sy in range(m):
            for d in range(4):
                if not visited[sx][sy][d]:
                    res = simulate(sx, sy, d, grid)
                    if res != 0:
                        answer.append(res)
    answer.sort()
    return answer