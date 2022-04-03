"""
8분 소요, 스스로 풂
핵심 포인트
1. A, B 종료 조건 만들기
2. 다음 라운드로 갔을 때 A와 B의 index 갱신하기
"""
def solution(N, A, B):
    round=1
    def nextRound(num):
        if num % 2 == 0:
            num//= 2
        else:
            num //= 2
            num += 1
        return num
    while True:
        if A%2==1 and B%2==0 and B-A==1:
            return round
        elif B%2==1 and A%2==0 and A-B==1:
            return round
        else:
            round+=1
            A, B = nextRound(A), nextRound(B)
