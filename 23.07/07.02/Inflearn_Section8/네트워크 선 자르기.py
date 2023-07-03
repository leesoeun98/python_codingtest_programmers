# 1. bottom-up : 점화식 찾기 (가장 작은 단위부터 크게 키우기)
# 2. top-down : 재귀로 풀기 (dfs로 풀자), dfs(7)은 dfs(6)+dfs(5)인걸 점화식은 동일
# for문 대신 재귀를 쓰고, 이미 dp 배열에 있는 값을 재활용해서 가닥 안뻗겠다! 단, dfs의 핵심은 종료 + 가지 cut

# n미터를 1, 2로 자르는 모든 가짓수
# dp의 핵심 => dp[n]을 dp[n-2]+2랑 dp[n-1]+1로 구분 지을 수 있음. 즉 이전 거에 1 혹은 2를 두면 이번에 구하려는 n이 됨
# 점화식 : f(n) = f(n-2)+f(n-1)
def problem1(input_value):
    dp = [0, 1, 2]
    for i in range(3, input_value + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[input_value]


dp2 = []


def problem2(input_value):
    global dp2
    dp2 = [0] * (input_value + 1)
    dfs(input_value)


def dfs(len):
    # 가지 cut하는 memoization이 정말 중요
    if dp2[len] > 0:
        return dp2[len]
    if len == 1 or len == 2:
        return len
    else:
        dp2[len] = dfs(len - 1) + dfs(len - 2)
        return dp2[len]
