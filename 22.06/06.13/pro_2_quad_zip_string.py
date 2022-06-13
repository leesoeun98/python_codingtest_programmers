"""
31분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 분할 정복, 어떻게 푸는지 대충 감은 왔는데 구현에 실패 (예전 코드에선 모두 같은 경우 10번을 반복해서 넣는 문제가 있었음)
2. s만큼 영역 만들고, 각 영역을 4등분해서 탐색하기
"""


def solution(arr):
    res = []

    # 분할 정복 문제, 4분할
    def slicing(x, y, length):
        nonlocal res
        start = arr[x][y]
        # s 부위를 4등분해서 탐색
        for i in range(x, x + length):
            for j in range(y, y + length):
                if start != arr[i][j]:
                    # 좌상
                    slicing(x, y, length // 2)
                    # 우상
                    slicing(x, y + length // 2, length // 2)
                    # 좌하
                    slicing(x + length // 2, y, length // 2)
                    # 우하
                    slicing(x + length // 2, y + length // 2, length // 2)
                    return
        res.append(start)

    slicing(0, 0, len(arr))
    return [res.count(0), res.count(1)]

