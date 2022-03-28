"""
10분 소요, 스스로 풂
핵심 포인트
1. dict 쓰기, 대신 변수 이름 주의
2. return 문에서 list comprehension 쓰기 (이때 slicing 주의)
"""
def solution(records):
    dic={}
    result=[]
    for record in records:
        sliced=record.split(' ')
        if sliced[0]=="Change":
            dic[sliced[1]]=sliced[2]
        elif sliced[0]=="Enter":
            dic[sliced[1]]=sliced[2]
            result.append(sliced[1]+"님이 들어왔습니다.")
        else:
            result.append(sliced[1]+"님이 나갔습니다.")
    return [item.replace(item.split("님")[0], dic[item.split("님")[0]]) for item in result]