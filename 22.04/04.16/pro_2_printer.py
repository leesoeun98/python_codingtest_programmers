"""
13분 소요, 스스로 풂, 디버깅 함
핵심 포인트
1. idx, priority같이 저장, copy
2. for last in printer_copy[:]: 이걸로 for문 순회, current[1] index 주의
3. flag 사용
4. 마지막에 lst.index(value) 에서 value는 list(filter)[0] 결과
"""
def solution(priorities, location):
    printer, res= [[idx, priority] for idx, priority in enumerate(priorities)], []
    printer_copy = printer.copy()
    while printer_copy:
        flag = True
        current = printer_copy.pop(0)
        for last in printer_copy[:]:
            if current[1]<last[1]:
                printer_copy.append(current)
                flag = False
                break
        if flag:
            res.append(current)
    return res.index(list(filter(lambda x:x[0]==location, res))[0])+1