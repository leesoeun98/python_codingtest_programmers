"""
8분 소요, 스스로 풂
핵심 포인트:
1. 3진법이나 0이 없음
=> 나머지가 0이면 res+="4" 하고 n//=3, n-=1
=> 나머지가 1, 2면 res+=str(remainder) 하고 n//=3
2. res[::-1]로 거꾸로 출력
3. res는 while문 밖에서 초기화해야 함 (안 그러면 while문에서 계속 초기화됨)
"""
def solution(n):
    res=""
    while n>0:
        remainder = n%3
        if remainder==0:
            res+="4"
            n //= 3
            n-=1
        else:
            res += str(remainder)
            n //= 3
    return int(res[::-1])
