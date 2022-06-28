"""
7분 소요, 스스로 풂
핵심 포인트
1. 단계별 구현력, 예외 처리
"""


def solution(places):
    res = []
    for place in places:
        people, flag = [], True
        # 사람 좌표 세기
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i, j])
        # 사람 간 맨해튼 거리 계산
        for i in range(len(people)):
            for j in range(len(people)):
                if i != j:
                    distance = abs(people[i][0] - people[j][0]) + abs(people[i][1] - people[j][1])
                    # 맨해튼 거리 2 이하면
                    if distance == 1:
                        flag = False
                        break
                    elif distance == 2:
                        # 파티션 확인
                        for x in range(min(people[i][0], people[j][0]), max(people[i][0], people[j][0]) + 1):
                            for y in range(min(people[i][1], people[j][1]), max(people[i][1], people[j][1]) + 1):
                                if [x, y] != [i, j] and place[x][y] == 'O':
                                    flag = False
                                    break
        res.append(0 if not flag else 1)
    return res