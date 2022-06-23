"""
4분 소요, 스스로 풀었으나 이전 코드 기억남
핵심 포인트
n이 10^7이라 절대 이중 for문 불가
-> for문 한번에 배열 만들어야 함
-> 규칙 123 / 223 / 333
-> 123에다가 0을 더하고 / 100 을 더하고 / 210을 더함
-> 각 숫자는 (i//n)-(i%n)임
"""

def solution(n, left, right):
    ans=[]
    for i in range(left, right+1):
        j = (i//n) - (i%n)
        if j<0:
            j=0
        ans.append((i%n)+1+j)
    return ans