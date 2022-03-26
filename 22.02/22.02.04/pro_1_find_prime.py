"""
에라토스테네스의 체 이용
"""
def solution(n):
    boolprime=[False, False]+[True]*(n-1)
    for i in range(2, n+1):
        if boolprime[i]:
            for j in range(i+i, n+1, i):
                boolprime[j]=False
    return len(list(filter(lambda x:x==True, boolprime)))
