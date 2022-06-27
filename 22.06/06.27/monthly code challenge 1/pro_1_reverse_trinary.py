"""
1분 소요, 스스로 풂
"""


def solution(n):
    res, ans="", 0
    while n>0:
        res+=str(n%3)
        n//=3
    for idx, i in enumerate(res[::-1]):
        ans+=(int(i)*(3**idx))
    return ans