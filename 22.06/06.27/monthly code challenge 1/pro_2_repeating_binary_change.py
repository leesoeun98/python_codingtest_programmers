"""
7분 소요, 스스로 풂
핵심 포인트
1. count 쓰기, slicing index 주의
"""


def solution(s):
    removed, cnt = 0, 0
    while s!='1':
        removed+=s.count('0')
        cnt+=1
        s=s.replace('0','')
        s=bin(len(s))[2:]
    return [cnt, removed]