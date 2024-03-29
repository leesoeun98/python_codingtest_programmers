# 최대 증가 수열같이 lst에서 i번째 원소까지 최대 증가 수열 길이
def problem(n, lst):
    dp = [0] * n
    for i in range(n):
        m = 0
        for j in range(i - 1, 0, -1):
            if lst[j] < lst[i] and m < dp[j]:
                m = dp[j]
        dp[i] = m + 1
    print(dp)
    return max(dp)


print(problem(100, [int(num) for num in "72 47 40 83 45 33 8 17 60 74 38 88 80 66 41 91 67 59 44 3 30 20 16 54 14 10 81 9 65 63 90 25 11 99 69 79 86 89 94 34 24 62 78 2 1 27 95 50 56 55 22 23 76 75 29 26 97 68 58 48 46 73 82 35 96 37 51 15 61 4 84 5 71 98 18 92 64 32 52 70 53 12 93 28 19 7 13 31 21 49 39 43 42 85 77 87 100 6 36 57".split(' ')]))
