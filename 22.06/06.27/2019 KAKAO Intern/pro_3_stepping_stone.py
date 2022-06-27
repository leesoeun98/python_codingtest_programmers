"""
25분 소요, 이전 코드 봄
핵심 포인트
1. 배열이 너무 커서 이중 for문 불가하면 이분 탐색
2. mid가 명수임 주석 참고
3. left, right 초기값 매우 주의 (stones 크기랑 동일하게)
"""


def solution(stones, k):
    # 배열 크기가 커서 이중 for문 절대 불가
    # 이런 경우 이분 탐색 필요
    left, right = 1, 200000000

    # 자동으로 while문은 종료됨
    while left <= right:
        # mid가 곧 지나갈 수 있는 명수
        temp_stone, mid, stone_cnt = stones.copy(), (left + right) // 2, 0

        # stone zero count -> stone_cnt
        for stone in temp_stone:
            if stone <= mid:
                stone_cnt += 1
                if stone_cnt >= k:
                    break
            else:
                stone_cnt = 0

        # left 갱신
        # stone_cnt가 k보다 많거나 같으면 앞으로 이동 (k랑 같으면 가장 가까운 돌로 가야해서 앞으로 가야 함)
        # stone_cnt가 k보다 작으면 뒤로 이동
        if stone_cnt < k:
            left = mid + 1
        else:
            right = mid - 1
    return left