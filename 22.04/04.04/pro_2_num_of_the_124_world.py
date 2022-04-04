"""
12분, 예전 코드 봄...
핵심 포인트
1. 3진법에서 0, 3 없앤 것
=> 3으로 나눈 나머지가 0이면 4로 바꾸고 -1로 자릿수 조절
"""
def solution(n):
    res=""
    while n>0:
        remainder = n%3
        n//=3
        if remainder==0:
            res+="4"
            n-=1
        else:
            res+=str(remainder)
    return res[::-1]