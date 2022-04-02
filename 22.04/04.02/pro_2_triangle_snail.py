"""
36분 소요, 다른 사람 코드 봄
핵심 포인트
1. 삼각형은 n번 방향을 바꿈 (i%3==0이면 아래, i%3==1이면 오른쪽, i%3==2면 위로 이동)
2. 한 방향으로 쭉 가되, range(i, n)까지만 가는 걸로 삼각형 사이즈가 점점 줄어들어 감소 형태
3. 좌표, 방향 설정만 완료하면 num+=1로 갱신만 해주면 됨
4. [[]] nested list를 flat하게 하는 방법 => sum(list, [])
"""
def solution(n):

    ans = [[0 for _ in range(1, i+1)] for i in range(1, n+1)]
    x, y = -1, 0
    num=1
    # n번 방향 바꿈 이때 i%3==0이면 아래, i%3==1이면 오른쪽, i%3==2면 위로 이동
    for i in range(n):
        # 한 방향으로 쭉 갈건데, 이때 점점 삼각형의 변의 사이즈가 작아질 것이므로 감소 형태
        for j in range(i, n):
            if i%3==0:
                x+=1
            elif i%3==1:
                y+=1
            else:
                x-=1
                y-=1
            ans[x][y]=num
            num+=1
    return sum(ans, [])