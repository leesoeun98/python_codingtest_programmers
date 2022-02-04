def gcd(n, m):
    if n%m==0:
        return m
    else:
        return gcd(m, n%m)

def solution(n, m):
    gcdnum= gcd(n, m)
    return [gcdnum, n*m/gcdnum]