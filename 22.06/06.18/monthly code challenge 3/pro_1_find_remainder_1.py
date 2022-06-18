"""
1분 소요, 스스로 풂 
"""
def solution(n):
    for i in range(1, n):
        if n%i==1:
            return i