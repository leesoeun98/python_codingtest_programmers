"""
33분 소요, 다른 사람 풀이 봄, dp문제 (이중 for문 불가)
핵심 포인트
1. dp...
"""
def solution(board):
    dp=[[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    max_ans=0
    for i in range(1, len(board)+1):
        for j in range(1, len(board[0])+1):
            if board[i-1][j-1]==1:
                dp[i][j]=min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
                if dp[i][j]>max_ans:
                    max_ans=dp[i][j]
    return max_ans**2