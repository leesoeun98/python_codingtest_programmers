"""
20분 소요, 이전 코드 봄 (시간 초과 때문에)
핵심 포인트
1. 시간 초과 안나게 continue 하는게 중요 함 + Counter 써야 시간 초과 안 남
2. 안되면 0 반환하는 것도 생각하기
"""

from collections import Counter


def solution(a):
    # 부분수열: 순서 유지
    # a의 부분 수열, 즉 a에서 순서는 유지하되 몇개 제외해서 가장 긴 수타 수열 만들기
    ans, intersect = -1, Counter(a)

    # 0부터 끝까지 순차적으로 접근해서 스타 수열 만들기
    # 스타 수열은 교집합이 공통으로 있어야 함
    for key, value in intersect.items():
        # 현재 스타 수열 길이보다 교집합 개수 적으면 탐색 불필요 (시간 초과 때문에)
        temp_ans, idx = 0, 0
        if ans >= value:
            continue
        while idx < len(a) - 1:
            if (a[idx] != key and a[idx + 1] != key) or a[idx] == a[idx + 1]:
                idx += 1
                continue
            else:
                idx += 2
                temp_ans += 1
        ans = max(ans, temp_ans)
    return 0 if ans == -1 else ans * 2

