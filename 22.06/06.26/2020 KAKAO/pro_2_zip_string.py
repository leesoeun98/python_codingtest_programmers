"""
9분 소요, 스스로 풀었으나 테스트케이스 봄
핵심 포인트
1. unit별로 문자열 쪼개서 연속되는 문자열 세기 (이 부분 구현하면 끝)
"""


def solution(s):
    ans = int(1e9)
    if len(s)==1:
        return 1
    for unit in range(1, len(s)):
        sliced = [s[i:i+unit] for i in range(0,len(s), unit)]
        before, cnt, res = sliced[0], 1, ""
        for i in range(1, len(sliced)):
            if sliced[i]==before:
                cnt+=1
            else:
                if cnt>1:
                    res+=(before+str(cnt))
                else:
                    res+=before
                cnt=1
                before = sliced[i]
        if cnt>1:
            res+=(before+str(cnt))
        else:
            res+=before
        ans = min(ans, len(res))
    return ans