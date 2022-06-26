"""
10분 소요, 스스로 풂
핵심 포인트
1. for문 한번에 res, dic에 모두 갱신 및 저장
2. 마지막에 list comprehension으로 res의 id를 name으로 replace
"""
def solution(record):
    dic, res={}, []
    for rec in record:
        rec = rec.split(' ')
        if rec[1] not in dic:
            dic[rec[1]] = ""
        if rec[0]=="Enter":
            dic[rec[1]] = rec[2]
            res.append(rec[1]+"님이 들어왔습니다.")
        elif rec[0]=="Leave":
            res.append(rec[1]+"님이 나갔습니다.")
        else:
             dic[rec[1]] = rec[2]
    return [row.replace(row.split('님')[0], dic[row.split('님')[0]] )for row in res]