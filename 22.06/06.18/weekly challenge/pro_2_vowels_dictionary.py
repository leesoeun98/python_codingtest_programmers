"""
40분 소요, 다른 사람 코드 봄
핵심 포인트:
1. 규칙 찾기 첫번째 자리간의 간격은 781, 그 다음은 156, 그 다음은 31, 그 다음은 6, 그 다음은 1
2. 각 자리 간격 * 알파벳 순서 (A는 0, E는 1, I는 2, O는 3, U는 4씩 곱하기) 그 다음 +1
"""


def solution(word):
    # 각 번째 자리의 간격은 781, 156, 31, 6, 1
    interval = [sum([5 ** i for i in range(n)]) for n in range(5, 0, -1)]
    ans = 0
    for i in range(len(word), 0, -1):
        if word[i - 1] == 'A':
            ans += 1
        elif word[i - 1] == 'E':
            ans += interval[i - 1] * 1 + 1
        elif word[i - 1] == 'I':
            ans += interval[i - 1] * 2 + 1
        elif word[i - 1] == 'O':
            ans += interval[i - 1] * 3 + 1
        elif word[i - 1] == 'U':
            ans += interval[i - 1] * 4 + 1
    return ans
