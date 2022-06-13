"""
12분 소요, 예전 코드 봄
핵심 포인트
1. 규칙 찾기 n이면 n번 방향이동, 각 방향을 이동할때마다 이동 칸 수 줄어듦 => 이중 for문
2. i%3으로 방향찾기, x, y 이동
3. 이중 list flat => itertools.chain.from_iterable() 이용
"""
# 이중 리스트 flat하게
import itertools
def solution(n):
    res=[[j for j in range(1, i+1)] for i in range(1, n+1)]
    x, y, num = -1,0,1
    # 한 방향으로 쭉, n이면 n번 방향 이동
    for i in range(n):
        # 한번 쭉 갈때 이동하는 칸 개수 (점점 줄어듦)
        for j in range(i, n):
            # 아래로
            if i%3==0:
                x+=1
            # 옆으로
            elif i%3==1:
                y+=1
            # 위로
            else:
                x-=1
                y-=1
            res[x][y]=num
            num+=1
    return list(itertools.chain.from_iterable(res))