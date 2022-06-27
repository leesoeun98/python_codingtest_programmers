"""
4분 소요, 스스로 풂
핵심 포인트
1. col고정, row만 이동
2. 인형 뽑으면 board 0으로 만들고 break 하기
"""


def solution(board, moves):
    stack, cnt = [], 0
    for move in moves:
        for j in range(len(board)):
            if board[j][move - 1] != 0:
                if len(stack) > 0 and stack[-1] == board[j][move - 1]:
                    stack.pop()
                    cnt += 2
                else:
                    stack.append(board[j][move - 1])
                board[j][move - 1] = 0
                break
    return cnt
