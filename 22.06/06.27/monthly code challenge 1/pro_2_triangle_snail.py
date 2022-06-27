"""
20분 소요, 스스로 풂
핵심 포인트
1. y=0 부터에 주의
2. board 생성 과정 및 flat 과정 주의
"""
from itertools import chain


def solution(n):
    board=[[0]*i for i in range(1, n+1)]
    x, y, num = -1,0,0
    for i in range(n):
        for j in range(i, n):
            if i%3==0:
                #아래
                x+=1
            elif i%3==1:
                #오른쪽
                y+=1
            elif i%3==2:
               # 대각선 위
                x-=1
                y-=1
            num+=1
            board[x][y]=num
    return list(chain.from_iterable(board))