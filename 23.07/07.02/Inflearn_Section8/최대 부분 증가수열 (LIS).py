# 배열을 바꾸지 않고, 배열 내에서 가장 크게 증가하는 원소 뽑아내기 (길이 반환)
# 접근법 : dp[i] = lst의 i번째 원소에 대해서 0~i-1 원소 중 i번째 원소보다 작고 dp값이 최대인 애 +1
def problem(n, lst):
    dp = [1]+[0]*(n-1)
    # i번째는 i-1보다 클 때, max(dp)+1
    for i in range(1, n):
        m = 0
        for j in range(i - 1, 0, -1):
            if lst[j] < lst[i] and dp[j] > m:
                m = dp[j]
        dp[i] = m + 1
    print(dp)
    return max(dp)
