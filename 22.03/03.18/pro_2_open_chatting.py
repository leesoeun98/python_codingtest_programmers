"""
5분 소요
dict를 쓰는게 핵심
"""
def solution(record):
    dict={}
    res=[]
    for rec in record:
        parsed=rec.split(" ")
        if len(parsed)==3:
            dict[parsed[1]]=parsed[2]
    for rec in record:
        parsed=rec.split(" ")
        if parsed[0]=="Enter":
            res.append(dict[parsed[1]]+"님이 들어왔습니다.")
        elif parsed[0]=="Leave":
            res.append(dict[parsed[1]]+"님이 나갔습니다.")
    return res
