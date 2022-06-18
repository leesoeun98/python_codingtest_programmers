"""
2분 소요, 스스로 풂
=> 팁: sqrt이용해서 제곱이면 약수 개수 홀수, 아니면 약수 개수 짝수
"""


def solution(left, right):
    ans = 0
    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
        if cnt % 2 == 0:
            ans += i
        else:
            ans -= i
    return ans
