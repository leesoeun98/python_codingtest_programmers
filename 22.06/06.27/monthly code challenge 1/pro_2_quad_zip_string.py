"""
3분 소요, 스스로 풂
핵심 포인트
1. 분할정복 문제 및 구현
"""
def solution(arr):
    answer = []
    # 분할정복 문제
    def slicing(x, y, length):
        nonlocal answer
        start=arr[x][y]
        for i in range(x, x+length):
            for j in range(y, y+length):
                if start!=arr[i][j]:
                    slicing(x, y, length//2)
                    slicing(x, y+length//2, length//2)
                    slicing(x+length//2, y, length//2)
                    slicing(x+length//2, y+length//2, length//2)
                    return
        answer.append(start)
    slicing(0,0,len(arr))
    return [answer.count(0), answer.count(1)]