"""
8분 소요, 스스로 풂
<핵심 포인트>
1. 파싱이 제일 중요, 문제 이해 및 len 기준 sorting
"""


def solution(s):
    sliced = s[1:-1].split("},")
    lst, ans = [], []
    for item in sliced:
        item = item.replace("{", "").replace("}", "")
        lst.append(list(map(int, item.split(','))))
    lst.sort(key=lambda x: len(x))
    for time in lst:
        for item in time:
            if item not in ans:
                ans.append(item)
    return ans
