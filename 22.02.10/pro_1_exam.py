"""from itertools import chain, repeat
def solution(answers):
    first = list(chain.from_iterable(repeat([1,2,3,4,5],2000)))
    second=list(chain.from_iterable(repeat([2,1,2,3,2,4,2,5],1250)))
    third = list(chain.from_iterable(repeat([3,3,1,1,2,2,4,4,5,5],1000)))
    dic={1:0, 2:0, 3:0}
    for i in range(len(answers)):
        if first[i]==answers[i]:
            dic[1]+=1
        if second[i]==answers[i]:
            dic[2]+=1
        if third[i]==answers[i]:
            dic[3]+=1
    return [k for k,v in dic.items() if max(dic.values()) == v]
"""
"""
dict에서 value max가 여러개일 때, 해당 dict의 key 모두 찾는 방법 기억하기 
문제 조건 잘 읽기 
미리 list 만들지 않고 index에 %로도 접근 가능
"""
def solution(answers):
    first=[1,2,3,4,5]
    second=[2,1,2,3,2,4,2,5]
    third=[3,3,1,1,2,2,4,4,5,5]
    dic = {1: 0, 2: 0, 3: 0}
    for idx, answer in enumerate(answers):
        if first[idx%len(first)]==answer:
            dic[1]+=1
        if second[idx%len(second)]==answer:
            dic[2]+=1
        if third[idx%len(third)]==answer:
            dic[3]+=1
    return [k for k,v in dic.items() if max(dic.values())==v]
