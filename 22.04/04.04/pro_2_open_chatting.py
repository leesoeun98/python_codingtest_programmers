"""
10분 소요, 스스로 풂
핵심 포인트
1. 각 Change, Enter, Leave별로 dic이랑 res에 저장
2. 마지막에 list comprhension으로 원하는 결과 만들기
"""
def solution(record):
    dic, res={}, []
    for row in record:
        if row.split(' ')[0]=="Change":
            dic[row.split(' ')[1]]=row.split(' ')[2]
        elif row.split(' ')[0]=="Enter":
            dic[row.split(' ')[1]]=row.split(' ')[2]
            res.append(row.split(' ')[1]+"님이 들어왔습니다.")
        elif row.split(' ')[0]=="Leave":
            res.append(row.split(' ')[1]+"님이 나갔습니다.")
    return list(dic[item.split("님")[0]]+"님"+item.split("님")[1] for item in res)
