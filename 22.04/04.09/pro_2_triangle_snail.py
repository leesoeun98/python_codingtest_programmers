"""
8분 소요, 예전 코드 봄
핵심 포인트
1. for j in range(i, n): 처럼 한 방향으로 쭉 가도 점점 작아지게
2. direction 3방향에 따라 if로 x, y 설정
3. [[]] nested list flat하게 itertools.chain(*list명)
"""
import itertools
def solution(n):
    triangle = [[0]*i for i in range(1, n+1)]
    x, y, num = -1, 0, 1
    for i in range(n):
        #한 방향으로 쭉
        for j in range(i, n):
            #아래로
            if i%3==0:
                x+=1
            #오른쪽
            elif i%3==1:
                y+=1
            #좌상향
            else:
                x-=1
                y-=1
            triangle[x][y]=num
            num+=1
    return list(itertools.chain(*triangle))