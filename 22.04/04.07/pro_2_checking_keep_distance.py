"""
15분 소요, 예전 코드 봄
실수 포인트
1. for 문 내 변수 이름 실수 (중복해서 씀)
2. 문제에서 주어진 문자열대로 안함
=> 이런 실수 진짜 하지 않기
"""
def solution(places):
    res=[]
    for place in places:
        people=[]
        for i in range(5):
            for j in range(5):
                if place[i][j]=="P":
                    people.append([i,j])
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
        res.append(1 if flag else 0 )
    return res



