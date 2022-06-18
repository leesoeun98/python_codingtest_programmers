"""
40분 소요, 이전 코드 봄
틀린 부분
1. 원소들 다 구해놓고 stars 그리는 걸 못함 => 실제 좌표처럼 여기서의 x는 row이므로 y 를 넣기
"""

from itertools import combinations


def solution(line):
    meeting_candidate = []
    meeting_final = []
    stars = []
    for combi in list(combinations(line, 2)):
        if combi[0][0] * combi[1][1] - combi[0][1] * combi[1][0] != 0:
            meeting_candidate.append([(combi[0][1] * combi[1][2] - combi[0][2] * combi[1][1]) / (
                        combi[0][0] * combi[1][1] - combi[0][1] * combi[1][0]),
                                      (combi[0][2] * combi[1][0] - combi[0][0] * combi[1][2]) / (
                                                  combi[0][0] * combi[1][1] - combi[0][1] * combi[1][0])])

    for x, y in meeting_candidate:
        if x.is_integer() and y.is_integer():
            meeting_final.append([int(x), int(y)])

    max_x, max_y, min_x, min_y = max([y for x, y in meeting_final]), max([x for x, y in meeting_final]), min(
        [y for x, y in meeting_final]), min([x for x, y in meeting_final])

    for i in range(min_x, max_x + 1):
        res = ""
        for j in range(min_y, max_y + 1):
            if [j, i] in meeting_final:
                res += "*"
            else:
                res += "."
        stars.append(res)
    return stars[::-1]