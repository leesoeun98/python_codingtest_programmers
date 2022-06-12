"""
11분 소요, 스스로 풂
주의할 점:
1. index에 주의, doll 개수임에 주의, len(dolls) 분기처리 주의
"""
def solution(board, moves):
    res, dolls = 0, []
    for move in moves:
        for j in range(len(board)):
            if board[j][move - 1] != 0:
                if len(dolls) > 0 and dolls[-1] == board[j][move - 1]:
                    res += 2
                    dolls.pop()
                elif len(dolls) == 0 or (len(dolls) > 0 and dolls[-1] != board[j][move - 1]):
                    dolls.append(board[j][move - 1])
                board[j][move - 1] = 0
                break
    return res


