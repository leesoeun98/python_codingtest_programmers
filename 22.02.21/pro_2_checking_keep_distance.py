"""
distance==2면 check해야하지만
distance==1면 그냥 바로 False => check를 하게 되면, 당연히 PP 이런식으로 붙은거라 p와p 사이에 O, P 이런게 없어서 check 통과해버림
매우 주의하기
*힌트 봤고, 정답까지 46분 걸림
"""
def solution(places):
    lst=[]
    for place in places:
        candidate=[]
        for i in range(5):
            for j in range(5):
                if place[i][j]=='P':
                    candidate.append([i,j])
        def check(candidate):
            for ctarget in candidate:
                for c in candidate:
                    if c!=ctarget:
                        distance=abs(c[0]-ctarget[0])+abs(c[1]-ctarget[1])
                        if distance==2:
                            for i in range(min(c[0], ctarget[0]), max(c[0], ctarget[0])+1):
                                for j in range(min(c[1], ctarget[1]), max(c[1], ctarget[1])+1):
                                    if [i,j] not in candidate:
                                        if place[i][j]=="O" or place[i][j]=="P":
                                            return False
                        if distance<2:
                            return False
            return True
        lst.append(0 if not check(candidate) else 1)
    return lst