"""
3분 소요, 스스로 풂
핵심 포인트
1. dic으로 id랑 name 갱신
2. for문 한번에 res에 모두 append하고 마지막에 replace + list comprehension
"""


def solution(record):
    dic, res={}, []
    for rec in record:
        lst = rec.split(' ')
        if lst[0]=="Enter":
            dic[lst[1]]=lst[2]
            res.append(lst[1]+"님이 들어왔습니다.")
        if lst[0]=="Leave":
            res.append(lst[1]+"님이 나갔습니다.")
        else:
            dic[lst[1]]=lst[2]
    return [row.replace(row.split("님")[0], dic[row.split("님")[0]]) for row in res]