"""
14분 소요, 스스로 풀었으나 테스트케이스 참고함
주의할 점:
index에 주의 20줄
"""

def solution(n, lost, reserve):
    students={}
    for i in range(1, n+1):
        students[i]=1
    for res in reserve:
        students[res]+=1
    for los in lost:
        students[los]-=1
    for k, v in students.items():
        if v==0:
            if k-1>0 and students[k-1]==2:
                students[k-1]-=1
                students[k]+=1
            elif k<n and students[k+1]==2:
                students[k+1]-=1
                students[k]+=1
    return len(list(k for k,v in students.items() if v!=0))
