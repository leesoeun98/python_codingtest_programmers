"""
9분 소요, 스스로 풂
핵심 포인트
1. location정보에 쉽게 접근하기 위해 enumerate로 idx, priority 정보 같이 저장
2. 각 item씩 pop해서 확인 후 append 혹은 빠져 나오기
3. printer[location]이 곧 item이 해당 item에 대한 index 찾기 result.index(printer[location])
"""
def solution(priorities, location):
    printer = [[priority, idx] for idx, priority in enumerate(priorities)]
    temp = printer.copy()
    result = []
    while temp:
        flag = True
        cur = temp.pop(0)
        for priority, idx in temp:
            if cur[0] < priority:
                temp.append(cur)
                flag = False
                break
        if flag:
            result.append(cur)
    return result.index(printer[location]) + 1
