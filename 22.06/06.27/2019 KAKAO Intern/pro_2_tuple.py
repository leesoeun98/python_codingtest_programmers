"""
3분 소요, 스스로 풂
핵심 포인트
1. 문제 이해 - 순서가 있는 튜플의 집합들이 주어질때, 집합의 각 원소들은 튜플의 순서와 관련있음 (즉, 원소 1개, 2개, 3개가 튜플 순서)
2. 문자열 처리가 중요
"""
def solution(s):
    lst = s[2:-2].split('},{')
    ans, res=[], []
    for ss in lst:
        ans.append(ss.split(','))
    ans = sorted(ans, key=lambda x:len(x))
    for row in ans:
        for item in row:
            if int(item) not in res:
                res.append(int(item))
    return res