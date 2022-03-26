"""
8분 소요, 스스로 풂
문제 이해하는데 조금 걸림 i번이 h-index의 후보가 된다는게 핵심 포인트
"""
def solution(citations):
    ans=0
    for i in range(0,len(citations)+1):
        fcount = len(list(filter(lambda x:x>=i, citations)))
        if fcount>=i:
            ans = max(i, ans)
    return ans
