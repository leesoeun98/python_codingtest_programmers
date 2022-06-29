"""
10분 소요, 이전 코드 봄
핵심 포인트
1. 규칙 찾기, 꼼꼼히 천천히 생각하기
"""
def solution(n, left, right):
    # 123 223 333
    # (i%n)에 000 100 210 더해야 함
    ans=[]
    for i in range(left, right+1):
        j = i//n - i%n
        if j<0:
            j=0
        ans.append(i%n+1+j)
    return ans