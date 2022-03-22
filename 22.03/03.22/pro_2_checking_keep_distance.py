"""
20분 소요, 스스로 풂
<핵심 포인트>
1. P인 좌표 모두 저장하기
2. 맨해튼 거리의 의미 찾기 (1이면 무조건 실패, 2면 판단해봐야 함, 2일때 판단하면 p 좌표 제외해야함)
3. 시간복잡도 줄이기 위해 최대한 break 쓰기
"""
def solution(places):
    lst = []
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    people.append([i, j])
        flag = True
        for i in range(len(people)):
            for j in range(i + 1, len(people)):
                distance = abs(people[i][0] - people[j][0]) + abs(people[i][1] - people[j][1])
                # distance가 1이면 바로 붙은거라 무조건 안 지킨거
                if distance == 1:
                    flag = False
                    break
                # distance가 2면 파티션 여부 확인 필요
                elif distance == 2:
                    for x in range(min(people[i][0], people[j][0]), max(people[i][0], people[j][0]) + 1):
                        for y in range(min(people[i][1], people[j][1]), max(people[i][1], people[j][1]) + 1):
                            if [x, y] != people[i] and [x, y] != people[j]:
                                if place[x][y] == 'O':
                                    flag = False
                                    break
        lst.append(0 if not flag else 1)
    return lst
