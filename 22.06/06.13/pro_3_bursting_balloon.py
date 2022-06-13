"""
23분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 투 포인터...이해해야 함
"""
def solution(a):
    # 투 포인터 문제
    # 문제 조건: 최대 한 번만 작은걸 터뜨릴 수 있다 == 큰게 터진다
    # 왼쪽 min 혹은 오른쪽 min 보다 target이 작아야 함
    # for문 안에서 배열의 앞, 뒤 각각 검사 진행
    # 가운데 수 는 중복되니까 False 배열 이용하기
    res=[False for _ in range(len(a))]
    min_front, min_rear = int(1e9), int(1e9)
    for i in range(len(a)):
        if a[i]<min_front:
            min_front=a[i]
            res[i]=True
        if a[-1-i]<min_rear:
            min_rear = a[-1-i]
            res[-1-i]=True
    return sum(res)