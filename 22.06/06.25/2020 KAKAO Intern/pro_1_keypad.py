"""
14분 소요, 스스로 풂
핵심 포인트
1. 구현력임 (left_idx, right_idx 매번 갱신하면서 distance 계산 후 res에 추가)
"""

def solution(numbers, hand):
    dic = {1: 'L', 4: 'L', 7: 'L', 3: 'R', 6: 'R', 9: 'R'}
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    res, left_idx, right_idx = "", '*', '#'
    for num in numbers:
        if num in dic:
            res += dic[num]
            if dic[num] == 'L':
                left_idx = num
            else:
                right_idx = num
        else:
            left, right, target = [], [], []
            for i in range(len(keypad)):
                for j in range(len(keypad[0])):
                    if keypad[i][j] == left_idx:
                        left.append([i, j])
                    if keypad[i][j] == num:
                        target.append([i, j])
                    if keypad[i][j] == right_idx:
                        right.append([i, j])
            left_distance = abs(target[0][0] - left[0][0]) + abs(target[0][1] - left[0][1])
            right_distance = abs(target[0][0] - right[0][0]) + abs(target[0][1] - right[0][1])
            if left_distance < right_distance or (left_distance == right_distance and hand == 'left'):
                res += 'L'
                left_idx = num
            else:
                res += 'R'
                right_idx = num
    return res


