"""
9분 소요, 스스로 풂
핵심 포인트
1. 문제 - 순서 있는, 중복 원소 없는 튜플 // 집합은 순서가 없으나 a1, a2 순으로 튜플이 유지 되어야 한다.
2. split 효율적으로 하기 위해 lstrip, rstrip, split쓰기
3. list comprehension으로 split한거 int로 변환해서 lst에 저장
4. lst를 각 원소 길이별로 sort 후, 각 원소들을 순서대로 담되 ans에 없어야 담기 
"""


def solution(s):
    s = s.lstrip("{{").rstrip("}}").split('},{')
    lst = [list(map(int, item.split(','))) for item in s]
    lst.sort(key=lambda x: len(x))
    ans = []
    for items in lst:
        for item in items:
            if item not in ans:
                ans.append(item)
    return ans
