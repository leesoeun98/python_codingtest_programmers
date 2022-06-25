"""
4분 소요, 스스로 풂
핵심 포인트
1. col, row 거꾸로 접근하기
2. board 갱신 후 break 하기
"""
def solution(board, moves):
    ans, cnt=[], 0
    for col in moves:
        for row in range(len(board)):
            if board[row][col-1]!=0:
                if len(ans)>0 and board[row][col-1]==ans[-1]:
                    ans.pop()
                    cnt+=2
                else:
                    ans.append(board[row][col-1])
                board[row][col-1]=0
                break
    return cnt