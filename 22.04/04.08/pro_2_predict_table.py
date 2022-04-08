"""
4분 소요, 스스로 풂
핵심 포인트
1. 수학 계산, 직접 해보기
2. round=1 부터 시작
3. nextRound함수는 한줄로 깔끔하게
"""
def nextRound(num):
        return num//2+1 if num%2==1 else num//2

def solution(N, A, B):
    round=1
    while True:
        if A%2==0 and B%2==1 and A-B==1:
            return round
        elif A%2==1 and B%2==0 and B-A==1:
            return round
        A, B = nextRound(A), nextRound(B)
        round+=1