"""
40분 소요, 다른 사람 코드 봄
핵심 포인트
1. 구현력 => 문제 코드 보고 그대로 풀기
1) 자물쇠 확장 시키고 가운데에 자물쇠 배치할 생각하기 (이동 쉽게 하기위해)
2) 자물쇠+열쇠 모두 1이면 열림 (check 함수)
3) 열쇠 넣기 (board에 key 더하기)
4) 열쇠 빼기 (board에 key 빼기)
5) rotate 90도 별로
6) solution 함수 내에서 4번 90도 회전하고, 각 회전별로 1부터 M+N까지 이동하면서 key attach, check, detach 순차적으로 하기
"""


def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[0] * (2 * M + N) for _ in range(2 * M + N)]
    # lock 2*M+N 크기로 확장 후 가운데에 실제 lock 두기
    for i in range(N):
        for j in range(N):
            board[i + M][j + M] = lock[i][j]

    # lock에 key 빼기
    def detach(x, y):
        nonlocal key, lock, M
        for i in range(M):
            for j in range(M):
                board[x + i][y + j] -= key[i][j]

    # lock에 key 빼기
    def attach(x, y):
        nonlocal key, lock, M
        for i in range(M):
            for j in range(M):
                board[x + i][y + j] += key[i][j]

    # 정중앙 모두 1인지 check
    # Key랑 lock 합쳐서 다 1 되면 풀린 것
    def check():
        nonlocal board, key, M
        for i in range(N):
            for j in range(N):
                if board[i + M][j + M] != 1:
                    return False
        return True

    # 회전
    def rotate_90(arr):
        res = [[0] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            temp = arr[i]
            for j in range(len(arr)):
                res[j][len(arr) - i - 1] = temp[j]
        return res

    # key 90도 4번 회전
    for i in range(4):
        key = rotate_90(key)
        # 이동
        for x in range(1, M + N):
            for y in range(1, M + N):
                # attach 해보기
                attach(x, y)
                if check():
                    return True
                detach(x, y)
    return False