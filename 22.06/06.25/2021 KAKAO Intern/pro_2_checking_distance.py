"""
9분 소요, 스스로 풂
핵심 포인트
=> 순서대로 구현력
=> 1. 사람 좌표 저장
=> 2. 사람별로 맨해튼 거리 확인, 파티션 확인
=> total_flag로 한번만 append
"""


def solution(places):
    res = []
    for place in places:
        people, total_flag = [], True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append([i, j])
        # 맨해튼 거리 확인
        for person1 in people:
            for person2 in people:
                if person1 != person2:
                    distance = abs(person1[0] - person2[0]) + abs(person1[1] - person2[1])
                    if distance == 1:
                        total_flag = False
                        break
                    elif distance == 2:
                        # 파티션 확인
                        for i in range(min(person1[0], person2[0]), max(person1[0], person2[0]) + 1):
                            for j in range(min(person1[1], person2[1]), max(person1[1], person2[1]) + 1):
                                if [i, j] != person1 and [i, j] != person2 and place[i][j] == 'O':
                                    total_flag = False
                                    break
        res.append(1 if total_flag else 0)
    return res


