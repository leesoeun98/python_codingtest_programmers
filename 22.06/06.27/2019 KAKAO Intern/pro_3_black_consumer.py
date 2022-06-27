"""
15분 소요, 이전 코드 봄
핵심 포인트
1. ban id 별 가능한 user id 목록 다 만들기
2. dfs로 가능한 조합 다 만들기
=> 1. ban id 길이만큼 탐색
=> 2. idx 별로 (ban id 별로) user들을 arr에 넣고 빼면서 dfs 만들기, 조합 생성
=> 3. ban id 길이만큼 다 탐색 시 arr이 set()에 없으면 add해서 조합 추가
"""
import re
from copy import deepcopy


def solution(user_id, banned_id):
    ans, candidate, ban_cnt = [], [], len(banned_id)

    # 각 user가 어느 ban에 들어갈지 결정해야 함 -> dfs
    def dfs(idx, arr):
        nonlocal ans, ban_cnt, candidate
        # ban id 길이만큼 다 탐색 시 종료
        if idx == len(candidate):
            if len(arr) == ban_cnt and arr not in ans:
                ans.append(deepcopy(arr))
            return
        # 조합 만들기
        # ban id 하나당 user id 후보들 모두 탐색
        for user in candidate[idx]:
            if user not in arr:
                # arr에 user 넣었다가
                arr.add(user)
                dfs(idx + 1, arr)
                # arr에 user 빼기
                arr.remove(user)

    # ban id가 될 수 있는 모든 후보 user id 만들기
    for ban in banned_id:
        # ban id *을 숫자나 영문으로 대체해서 모든 경우의 수 만듦
        ban = re.compile("^" + ban.replace('*', "([0-9]|[a-z])") + "$")
        temp = set()
        for user in user_id:
            # user가 ban에 매칭되면 temp에 저장
            if ban.match(user):
                temp.add(user)
        candidate.append(temp)

    dfs(0, set())
    return len(ans)