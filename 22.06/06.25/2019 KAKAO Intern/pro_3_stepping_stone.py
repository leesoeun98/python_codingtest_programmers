"""
25분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 그냥 while문 돌면 정확성만 통과
2. 이런 경우 이분탐색을 써야 효율성 통과 가능
=> 1. stone_cnt 매번 세기 (mid명이 각 stone 통과 할 수 있는지 보기)
=> 2. stone_cnt가 k보다 크거나 같으면 right = mid - 1
=> 3. stone_cnt가 k보다 작으면 left = mid + 1
"""


def solution(stones, k):
    left, right = 1, 200000000
    while left <= right:
        mid = (left + right) // 2
        temp = stones.copy()
        stone_cnt = 0
        # stone_cnt 세기
        for num in temp:
            # mid명이 각 num을 통과할 수 있는지 보고, 통과 못하면 stone_cnt+1
            if num <= mid:
                stone_cnt += 1
            else:
                stone_cnt = 0
            if stone_cnt >= k:
                break
        # k가 stone_cnt보다 크면 left 갱신
        if k > stone_cnt:
            left = mid + 1
        else:
            right = mid - 1
    return left