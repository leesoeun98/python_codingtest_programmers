def solution(n):
    ternary=[]
    ans=0
    while n:
        ternary.append(n%3)
        n//=3
    for idx, t in enumerate(ternary[::-1]):
        ans+=t*3**idx
    return ans