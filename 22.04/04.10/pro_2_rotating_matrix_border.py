"""
1시간 소요, min 구하는데서 예전 코드 봄 (그래도 행렬 돌리는건 스스로 함)
핵심 포인트
1. 행렬 직접 다 돌리는거 구현해보기
2. min은 set이용해서 바꾸는거마다 다 집어넣으면 됨 => 시간 덜 걸리게 for문 한번 내에서 넣기
3. 시간 초과 -> deepcopy 절대 금지
4. 컴파일 에러 -> 마지막 matrix[startx][endy], matrix[startx+1][endy] = matrix[startx+1][endy], matrix[startx][endy]
        여기서 index 에러 난 듯
"""
def solution(rows, colums, queries):
    matrix, num, res =[[0]*colums for _ in range(rows)], 1, []
    for i in range(rows):
        for j in range(colums):
            matrix[i][j]=num
            num+=1
    for query in queries:
        temp=set()
        startx, starty, endx, endy = query
        startx-=1
        starty-=1
        endx-=1
        endy-=1
        #위 <- 방향 이동
        for i in range(endy, starty, -1):
            matrix[startx][i], matrix[startx][i-1]= matrix[startx][i-1], matrix[startx][i]
            temp.add(matrix[startx][i])
            temp.add(matrix[startx][i-1])
        #좌 아래 방향 이동
        for i in range(startx, endx):
            matrix[i][starty], matrix[i+1][starty] = matrix[i+1][starty], matrix[i][starty]
            temp.add(matrix[i][starty])
            temp.add(matrix[i+1][starty])
        #아래 -> 방향 이동
        for i in range(starty, endy):
            matrix[endx][i], matrix[endx][i+1] = matrix[endx][i+1], matrix[endx][i]
            temp.add(matrix[endx][i])
            temp.add(matrix[endx][i+1])
        #오른쪽 위 방향 이동
        for i in range(endx, startx, -1):
            matrix[i][endy], matrix[i-1][endy] = matrix[i-1][endy], matrix[i][endy]
            temp.add(matrix[i][endy])
            temp.add(matrix[i-1][endy])
        matrix[startx][endy], matrix[startx+1][endy] = matrix[startx+1][endy], matrix[startx][endy]
        temp.add(matrix[startx][endy])
        temp.add(matrix[startx+1][endy])
        res.append(min(list(temp)))
    return res