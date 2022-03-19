"""
예전 풀이 봄
핵심 포인트
1. 3진법인데, 0이랑 3이 없어서 4로 대체 해야함
=> 예로 20(3)이면 14로 바꿔야 하므로 n-1하고 무조건 끝자리르 4로 끝나게 변환
2. 진법 계산 후 결과는 거꾸로 출력해야 함
"""
def solution(n):
    ans=""
    while n!=0:
        remainder=n%3
        n//=3
        if remainder==0:
            n-=1
            ans+="4"
        else:
            ans+=str(remainder)
    return ans[::-1]
