# 1차 성공 : 24분 소요, 다른 사람 풀이 봄
# 가로2 세로1인 직사각형으로 3*n을 채울 수 있는 가지 수 % 1,000,000,007 return
# dp, 점화식 찾는게 매우 어려웠음 (다른 사람 풀이 참고)
dp = [3, 11]


def solution(n):
    for i in range(2, (n // 2) + 1):
        dp.append(dp[i - 1] * 3 + 2 * (sum(dp[:i - 1])) + 2)
    return dp[-2] % 1000000007
