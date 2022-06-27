"""
1시간 8분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 구현력
=> 비슷하게 접근은 했는데, 차근히 좀 더 생각을 해야하고 코드를 깔끔하게 쓰는법 정리해야 함
=> 설치시 설치하고 impossible이면 제거, 제거 시 제거하고 impossible이면 설치
"""


def solution(n, build_frame):
    board = set()

    def impossible():
        nonlocal board
        for x, y, a in board:
            # 기둥
            if a == 0:
                if y != 0 and (x - 1, y, 1) not in board and (x, y - 1, 0) not in board and (x, y, 1) not in board:
                    return True
            # 보
            else:
                if (x, y - 1, 0) not in board and (x + 1, y - 1, 0) not in board and not (
                        (x - 1, y, 1) in board and (x + 1, y, 1) in board):
                    return True

    for x, y, a, b in build_frame:
        item = (x, y, a)
        # 설치
        if b == 1:
            board.add(item)
            if impossible():
                board.remove(item)
        # 삭제
        elif item in board:
            board.remove(item)
            if impossible():
                board.add(item)
    return sorted(map(list, board), key=lambda x: (x[0], x[1], x[2]))
