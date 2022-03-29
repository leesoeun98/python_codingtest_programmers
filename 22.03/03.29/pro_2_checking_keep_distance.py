"""
14분 소요, 한 번 틀려서 예전 풀이 봄
핵심 포인트
1. 사람이 앉은 좌표들 다 뽑아 놓기
2. 각 사람들이 다른 사람들 과의 맨해튼 거리 구하기
=> 맨해튼 거리가 1이면 무조건 0 (바로 붙은거라)
=> 맨해튼 거리가 2이면 파티션에 따라 판단 해야 함
* break문 쓰면 for문 전체 빠져나오므로 flag 로 두기, flag는 실패할 경우에만 바꾸도록 해서 한 번이라도 실패 시 False이도록 하기
* 마지막 파티션 확인할 때 for문 범위 틀림 => 출력으로 다시 확인하는 습관 갖기
"""
def solution(places):
    res=[]
    for place in places:
        people=[]
        for i in range(5):
            for j in range(5):
                if place[i][j]=="P":
                    people.append([i, j])
        flag = True
        for i in range(len(people)):
            for j in range(i+1, len(people)):
                distance = abs(people[i][0]-people[j][0])+abs(people[i][1]-people[j][1])
                if distance==1:
                    flag = False
                elif distance==2:
                    for row in range(min(people[i][0], people[j][0]), max(people[i][0], people[j][0])+1):
                        for col in range(min(people[i][1], people[j][1]), max(people[i][1], people[j][1])+1):
                            if [row, col]!=people[i] and [row, col]!=people[j] and place[row][col]=="O":
                                flag = False
        res.append(0 if not flag else 1)
    return res
