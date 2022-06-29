"""
1분 소요, 스스로 풂
핵심 포인트
1. dict 이용해서 replace
"""


def solution(s):
    dic={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for key, value in dic.items():
        s = s.replace(key, str(value))
    return int(s)