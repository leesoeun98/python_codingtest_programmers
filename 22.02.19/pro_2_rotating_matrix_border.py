"""
row, column , x, y 모두 헷갈리지 않기
rotate의 경우 반대순서로 돌려야 함
(상단가로->우측세로->하단가로->좌측세로 순으로 돌리는거면, for문의 경우 좌측세로->하단가로->우측세로->상단가로)
마지막에도 swap 해주는거 잊지 말기 (출력해보고 swap 체크하기)
"""
def make_matrix(rows, columns):
    matrix = [[i for i in range(1, columns + 1)] for _ in range(rows)]
    for i in range(1, rows):
        for j in range(1, columns + 1):
            matrix[i][j - 1] = matrix[i - 1][j - 1] + columns
    return matrix

def rotate(matrix, query):
    x1, y1, x2, y2 = query
    x1-=1
    y1-=1
    x2-=1
    y2-=1
    mins=[]
    for i in range(x1, x2):
        matrix[i][y1], matrix[i+1][y1] = matrix[i+1][y1], matrix[i][y1]
        mins.append(matrix[i][y1])
        mins.append(matrix[i+1][y1])
    for i in range(y1, y2):
        matrix[x2][i], matrix[x2][i+1]= matrix[x2][i+1], matrix[x2][i]
        mins.append(matrix[x2][i])
        mins.append(matrix[x2][i+1])
    for i in range(x2, x1, -1):
        matrix[i][y2], matrix[i-1][y2] = matrix[i-1][y2], matrix[i][y2]
        mins.append(matrix[i][y2])
        mins.append(matrix[i-1][y2])
    for i in range(y2, y1, -1):
        matrix[x1][i], matrix[x1][i-1] = matrix[x1][i-1], matrix[x1][i]
        mins.append(matrix[x1][i])
        mins.append(matrix[x1][i-1])
    matrix[x1][y1], matrix[x1][y1+1] = matrix[x1][y1+1], matrix[x1][y1]
    mins.append(matrix[x1][y1])
    mins.append(matrix[x1][y1+1])
    smin = set(mins)
    return matrix, min(smin)

def solution(rows, columns, queries):
    matrix = make_matrix(rows, columns)
    res=[]
    for q in queries:
        matrix, minnum = rotate(matrix, q)
        res.append(minnum)
    return res
