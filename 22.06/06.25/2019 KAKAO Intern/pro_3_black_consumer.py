"""
1시간 소요, 다른 사람 풀이 봄 (dfs까진 하고 그 뒤를 못함)
핵심 포인트
ban에 대해 user 검색
1. ban re compile 만들기
2. ban에 user가 해당되면 temp set에 user 넣고 (즉, ban id별 가능한 user id 다 넣어놓고)
3. candidate(total 조합)에 temp append
4. dfs로 조합 만들어서 ans 에 넣기 (dfs로는 각각의 combi 만들기)
"""
import re
from copy import deepcopy

def solution(user_id, banned_id):
    ans, candidate, ban_cnt = [], [], len(banned_id)

    def dfs(idx, candidate, arr):
        nonlocal ban_cnt, ans
        # 조합 끝까지 다 본 경우
        if idx == len(candidate):
            if len(arr)==ban_cnt and arr not in ans:
                ans.append(deepcopy(arr))
            return
        # 조합 만들기
        for user in candidate[idx]:
            if user not in arr:
                arr.add(user)
                dfs(idx+1, candidate, arr)
                arr.remove(user)

    for i in range(len(banned_id)):
        # banned_id[i]로 시작하되 *을 영소문자, 숫자로 대체
        banned_id[i] = re.compile("^"+banned_id[i].replace('*',"([0-9]|[a-z])")+"$")
        temp=set()
        # ban별 가능한 user id 저장
        for user in user_id:
            if banned_id[i].match(user):
                temp.add(user)
        candidate.append(temp)
    dfs(0,candidate, set())
    return len(ans)