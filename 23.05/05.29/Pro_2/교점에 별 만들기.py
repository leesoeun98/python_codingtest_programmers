# 50분 소요, 예전 코드 봄
# 1차 실패 : 별은 맞게 그린거 같은데 교점에서 틀린 듯
# 2차 시도 : 별 자체를 잘못 그림 (좌표 변형에 주의하자), 예전 코드 봄

from itertools import combinations


def solution(line):
    dots = []
    # nC2로 교점개수 다 구한 후, 정수인 교점들만 저장
    for combi in list(combinations(line, 2)):
        a, b, e = combi[0]
        c, d, f = combi[1]
        if a * d - b * c != 0:
            x, y = (b * f - e * d) / (a * d - b * c), (e * c - a * f) / (a * d - b * c)
            if x.is_integer() and y.is_integer() and [int(x), int(y)] not in dots:
                dots.append([int(x), int(y)])
    # 별 그리기
    minX, maxX, minY, maxY = min([y for x, y in dots]), max([y for x, y in dots]), min([x for x, y in dots]), max(
        [x for x, y in dots])
    result=[]
    for i in range(minX, maxX+1):
        res=""
        for j in range(minY, maxY+1):
            if [j, i] in dots:
                res+="*"
            else:
                res+="."
        result.append(res)
    return result[::-1]