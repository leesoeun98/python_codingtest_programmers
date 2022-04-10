"""
21분 소요, 스스로 풂
핵심 포인트
1. sort하고 가장 무거운 애, 가장 가벼운 애 같이 태워보기
2. 같이 못타면 가장 무거운 애 빼기
3. 반복
4. 시간 초과 피하기 위해 deque사용
"""
from collections import deque
def solution(people, limit):
    people = sorted(people)
    deq = deque(people)
    count= 0
    while deq:
        if len(deq)>1:
            if deq[0]+deq[-1]<=limit:
                deq.popleft()
                deq.pop()
            else:
                deq.pop()
        else:
            deq.pop()
        count+=1
    return count

