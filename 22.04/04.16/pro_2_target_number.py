"""
7분 소요, 스스로 풂
핵심 포인트
1. dfs에 nonlocal로 count 접근
2. dfs에 종료조건 확실히, count+=1 조건도 명확하게
3. dfs(0,0)으로 해야 +-numbers[0]부터 가능함
"""


def solution(numbers, target):
    count = 0

    def dfs(depth, res):
        nonlocal count
        if depth == len(numbers):
            if res == target:
                count += 1
            return
        dfs(depth + 1, res + numbers[depth])
        dfs(depth + 1, res - numbers[depth])

    dfs(0, 0)
    return count


