"""
20분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 스타 수열을 직접 만들되, 교집합이 나타난 횟수 *2 가 스타 수열의 길이가 됨
=> Counter로 각 원소 개수 세기
=> 현재 교집합이 나타난 횟수보다 count 수가 적으면 탐색 x
=> idx, common_cnt로 스타수열 만들고 위배 시 idx+1해서 a[idx+1:]에서 스타수열 다시 탐색
=> 맞으면 common_cnt+1 idx+2로 수열 만들기
"""
from collections import Counter


def solution(a):
    elements = Counter(a)
    answer = -1

    # 각 원소별로 탐색
    for k in elements.keys():
        # answer보다 k등장 횟수가 더 작으면 탐색이 필요 없음
        if elements[k] <= answer:
            continue
        # 공통 원소 수
        common_cnt, idx = 0, 0
        # 스타수열 규칙에 맞는지 확인 (위배 시 idx+1로 남은 수열들로 재확인)
        while idx < len(a) - 1:
            if (a[idx] != k and a[idx + 1] != k) or a[idx] == a[idx + 1]:
                idx += 1
                continue
            # 규칙에 맞으면 idx+2, common_cnt+1
            idx += 2
            common_cnt += 1
        answer = max(answer, common_cnt)
    return 0 if answer == -1 else answer * 2

