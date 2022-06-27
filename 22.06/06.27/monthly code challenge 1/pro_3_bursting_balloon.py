"""
6분 소요, 스스로 풂 (근데 이전 코드 기억함)
핵심 포인트
1. 문제 이해.. 주석을 참고

"""


def solution(a):
    # 큰 수가 무조건 터지고, 작은건 한 번만 터질 수 있음
    # 특정 수에 대해 양쪽이 둘다 크면 해당 수는 남을 수 있음
    res = [False] * len(a)
    front_min, rear_min = int(1e9), int(1e9)
    for i in range(len(a)):
        if front_min > a[i]:
            front_min = a[i]
            res[i] = True
        if rear_min > a[len(a) - i - 1]:
            rear_min = a[len(a) - i - 1]
            res[len(a) - i - 1] = True
    return sum(res)
