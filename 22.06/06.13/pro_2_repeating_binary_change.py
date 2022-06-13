"""
7분 소요, 스스로 풂
핵심 포인트
1. count로 0 세기
2. 문제 잘읽기!! 길이를 이진변환 하는 것
3. 이진 변환은 bin(int)[:2] 임에 주의
"""


def solution(s):
    removed, cnt = 0, 0
    while s != '1':
        removed += s.count('0')
        cnt += 1
        s = s.replace('0', '')
        s = str(bin(int(len(s)))[2:])
    return [cnt, removed]
