"""
12분 소요, 스스로 풂
핵심 포인트
1. while문으로 반복, 종료 조건 확실히
2. 문제 잘읽기 len(s)임
3. bin결과는 str임에 주의
"""
def solution(s):
    count, removed_zero = 0,0
    while s!="1":
        removed_zero+=s.count('0')
        count+=1
        s = s.replace("0", "")
        s = bin(len(s))[2:]
    return [count, removed_zero]