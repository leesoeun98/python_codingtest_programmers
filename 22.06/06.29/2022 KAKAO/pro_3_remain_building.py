"""
12분 소요, 정확도는 스스로 푼 코드 모두 통과
최대한 for문 수 줄이기 위해 flat하게 처리하자는 발상
=> 효율성은 절대 안됨. 누적합으로 가야 함
21:24
"""
def solution(board, skill):
    answer = 0
    tmp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]
    for t, r1, c1, r2, c2, d in skill:
        #누적합 기록 (누적합 시 시작, 끝+1에 넣기)
        tmp[r1][c1] +=d if t==2 else -d
        tmp[r1][c2+1] += -d if t==2 else d
        tmp[r2+1][c1] += -d if t==2 else d
        tmp[r2+1][c2+1] += d if t==2 else -d
    # col 누적합
    for j in range(len(tmp[0])-1):
        for i in range(len(tmp)-1):
            tmp[i+1][j]+=tmp[i][j]
    # row 누적합
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1]+=tmp[i][j]
    # 기존 배열과 합치기
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=tmp[i][j]
            if board[i][j]>0:
                answer+=1
    return answer

"""
from itertools import chain
def solution(board, skill):
    flat_board = list(chain.from_iterable(board))
    n, m = len(board), len(board[0])
    for t, r1, c1, r2, c2, d in skill:
        if t==1:
            for i in range(len(flat_board)):
                if c1<=i%n<=c2 and r1<=i//n<=r2:
                    flat_board[i]-=d
        else:
            for i in range(len(flat_board)):
                if c1<=i%n<=c2 and r1<=i//n<=r2:
                    flat_board[i]+=d
    return len([r for r in flat_board if r>0])
"""