"""
17분 소요, 예전코드 봄
틀린 부분
1. chain.from_iterable을 써야 함 => 왜???? 메모리 때문인듯.. 크게 반복해야 할땐 chain.from_iterable과 repeat 쓰자
"""
from itertools import chain, repeat


def solution(answers):
    dic = {1: 0, 2: 0, 3: 0}
    first = list(chain.from_iterable(repeat([1,2,3,4,5],2000)))
    second=list(chain.from_iterable(repeat([2,1,2,3,2,4,2,5],1250)))
    third = list(chain.from_iterable(repeat([3,3,1,1,2,2,4,4,5,5],1000)))
    for i in range(len(answers)):
        if first[i] == answers[i]:
            dic[1] += 1
        if second[i] == answers[i]:
            dic[2] += 1
        if third[i] == answers[i]:
            dic[3] += 1

    return [k for k, v in dic.items() if max(dic.values()) == v]