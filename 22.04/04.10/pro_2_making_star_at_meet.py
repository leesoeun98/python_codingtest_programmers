"""
18분 소요, 스스로 풂
핵심포인트
1. int 교점 다 구하기
2. minX, maxX, minY, maxY 구하기
3. for j in range(minX, maxX+1):
    for i in range(minY, maxY+1): 로 별 그리기 (X, Y 반대임에 주의)
"""
def solution(lines):
    meets, stars = set(), []
    for i in range(len(lines)):
        for j in range(len(lines)):
            if i!=j and lines[i][0]*lines[j][1]-lines[i][1]*lines[j][0]!=0:
                x = (lines[i][1]*lines[j][2]-lines[i][2]*lines[j][1])/(lines[i][0]*lines[j][1]-lines[i][1]*lines[j][0])
                y = (lines[i][2]*lines[j][0]-lines[i][0]*lines[j][2])/(lines[i][0]*lines[j][1]-lines[i][1]*lines[j][0])
                if int(x)==x and int(y)==y:
                    meets.add((int(x), int(y)))
    minX, minY = min([x[1] for x in list(meets)]), min([x[0] for x in list(meets)])
    maxX, maxY = max([x[1] for x in list(meets)]), max([x[0] for x in list(meets)])
    for j in range(minX, maxX+1):
        res=""
        for i in range(minY, maxY+1):
            if (i, j) in meets:
                res+="*"
            else:
                res+="."
        stars.append(res)
    return stars[::-1]