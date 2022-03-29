"""
10분 소요, 스스로 풂
핵심 포인트:
1. 반복문 다 돌지 말고 만족하는 조건 있으면 break로 빠져나와야 시간 초과 안 뜸
2. locatoin 알아야 하니까 enumerate로 [idx, priority] 배열 저장하기
3. copy해서 다 pop 시키고, printer[location]으로 item추출해서 해당 index 찾기
"""
def solution(priorities, location):
    printer = [[idx, priority] for idx, priority in enumerate(priorities)]
    result=[]
    printer_copy = printer.copy()
    while printer_copy:
        cur = printer_copy.pop(0)
        flag = False
        for idx, priority in printer_copy:
            if priority>cur[1]:
                flag = True
                printer_copy.append(cur)
                break
        if not flag:
            result.append(cur)
    return result.index(printer[location])+1
