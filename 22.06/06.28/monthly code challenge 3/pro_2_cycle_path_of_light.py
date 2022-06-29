"""
26분 소요, 이전 코드 봄
핵심 포인트
1. simulate 함수에 주의
"""
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def solution(grid):
    light = [[[False] * 4 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # 빛 출발 시 사이클 시물레이션
    def simulate(x, y, di):
        nonlocal light
        nx, ny, nd = x, y, di
        light[nx][ny][nd] = True
        length = 0
        while True:
            # 좌표 갱신
            nx = (nx + dx[nd]) % len(grid)
            ny = (ny + dy[nd]) % len(grid[0])
            length += 1
            # 방향 갱신
            if grid[nx][ny] == 'L':
                nd = (nd - 1) % 4
            elif grid[nx][ny] == 'R':
                nd = (nd + 1) % 4
            # 사이클 종료
            if light[nx][ny][nd]:
                if [nx, ny, nd] == [x, y, di]:
                    return length
                else:
                    return 0
            light[nx][ny][nd] = True

    answer = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                # i j 에서 d 방향으로 빛 출발
                if not light[i][j][d]:
                    length = simulate(i, j, d)
                    if length != 0:
                        answer.append(length)
    return sorted(answer)
