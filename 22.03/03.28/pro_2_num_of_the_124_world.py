"""
7분 소요, 예전 코드 봄
핵심 포인트
1. 자릿수 이해해야 함 (0, 3이 없으므로 0으로 나누어지면 4를 ans에 더하고 -1 을 해야 자릿수 줄 일 수 있음)
"""
def solution(n):
    ans=""
    while n>0:
        remainder = n % 3
        n//=3
        if remainder==0:
            ans+="4"
            n-=1
        else:
            ans+=str(remainder)
    return ans[::-1]
