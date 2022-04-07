"""
6분 소요, 스스로 풂
핵심 포인트
1. 각 location, priority 정보 같이 저장하는 list 생성
2. printers_copy 끝날때까지 반복해서 printed에 넣고
3. printed에서 개체에 대한 index 반환
"""
def solution(priorities, location):
    count=1
    printers = [[idx, priority] for idx, priority in enumerate(priorities)]
    printers_copy = printers.copy()
    printed=[]
    while printers_copy:
        cur = printers_copy.pop(0)
        flag = True
        for printer in printers_copy:
            if cur[1]<printer[1]:
                flag = False
                printers_copy.append(cur)
                count+=1
                break
        if flag:
            printed.append(cur)
    return printed.index(printers[location])+1
