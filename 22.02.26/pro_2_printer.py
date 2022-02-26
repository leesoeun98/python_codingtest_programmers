"""
내 이전 코드 봄..ㅠㅠ
deque가 끝날때까지 돌리고 싶다면 while 쓰기, if문 후 break하기
"""
from collections import deque
def solution(priorities, location):
    printer=[]
    for idx, prior in enumerate(priorities):
        printer.append([idx, prior])
    deq = deque(printer)
    order=[]
    while deq:
        cur = deq.popleft()
        order.append(cur)
        for d in deq:
            if cur[1]<d[1]:
                deq.append(cur)
                order.pop()
                break
    return order.index(printer[location])+1