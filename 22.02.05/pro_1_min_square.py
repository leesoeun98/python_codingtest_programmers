"""
두 길이를 비교해서 항상 큰게 가로, 항상 작은게 세로라고 한다면
=> 가로 중 최대, 세로 중 최대의 곱이 답이 된다.
"""

def solution(sizes):
    return max(max(x) for x in sizes)*max(min(x) for x in sizes)
"""
def solution(sizes):
    mostBig, mostSmall = 0,0
    for row, col in sizes:
        if mostBig<max(row, col):
            mostBig = max(row, col)
        if mostSmall<min(row, col):
            mostSmall = min(row, col)
    return mostBig*mostSmall
"""

