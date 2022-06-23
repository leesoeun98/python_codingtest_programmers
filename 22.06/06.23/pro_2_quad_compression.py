"""
5분 소요, 스스로 풀었으나 이전 코드가 기억남
핵심 포인트
1. 분할 정복 문제 4개로 쪼개고 return해서 재귀를 끝내주기, slicing 후에 ans에 start append
"""
def solution(arr):
    ans = []

    def slicing(x, y, length):
        start = arr[x][y]
        for i in range(x, x + length):
            for j in range(y, y + length):
                if arr[i][j] != start:
                    slicing(x, y, length // 2)
                    slicing(x, y + length // 2, length // 2)
                    slicing(x + length // 2, y, length // 2)
                    slicing(x + length // 2, y + length // 2, length // 2)
                    return
        ans.append(start)

    slicing(0, 0, len(arr))
    return [ans.count(0), ans.count(1)]
