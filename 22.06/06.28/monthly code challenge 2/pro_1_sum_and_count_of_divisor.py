"""
3분 소요, 스스로 풂
핵심 포인트
제곱수면 약수개수가 홀수임을 이용
"""
import math
def solution(left, right):
    ans=0
    for num in range(left, right+1):
        if math.sqrt(num)==int(math.sqrt(num)):
            ans-=num
        else:
            ans+=num
    return ans