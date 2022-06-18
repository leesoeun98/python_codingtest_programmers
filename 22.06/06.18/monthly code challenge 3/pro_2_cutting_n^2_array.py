"""
33분 소요, 다른 사람 코드 봄
핵심 포인트
1. n이 10^7까지이므로 시간초과에 주의 => 이중 for문 절대 불가
2. 1, 2, .., n 까지 순서대로 배치를 하되 각각 더해져야 하는 수가 있음
=> (i//n)-(i%n) 만큼 더하되 음수면 0을 더하기
"""
def solution(n, left, right):
    lst=[]
    for i in range(left, right+1):
        j=(i//n)-(i%n)
        if j<0:
            j=0
        lst.append(i%n+1+j)
    return lst