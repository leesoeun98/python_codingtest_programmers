# bottom-up (점화식)
def problem1(n):
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


# top-down (dfs)
dp2 = []


def problem2(n):
    global dp2
    dp2 = [0] * (n + 1)
    return dfs(n)


def dfs(n):
    if dp2[n] > 0:
        return dp2[n]
    # 종료
    if n == 1 or n == 2:
        return n
    else:
        dp2[n] = dfs(n - 1) + dfs(n - 2)
        return dp2[n]
