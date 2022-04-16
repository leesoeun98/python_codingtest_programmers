"""
7분 소요, 스스로 풂
핵심 포인트
1. bridge_length에 해당하는 brdige만들고 truck_weights 원소 있을동안 매번 pop, append 반복
2. 시간 복잡도 줄이기 위해 bridge_weight 변수 사용
3. 마지막 truck이 끝나면 time+bridge_length 반환
"""
from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge= deque([0]*bridge_length)
    bridge_weight = 0
    time=0
    while truck_weights:
        left = bridge.popleft()
        bridge_weight-=left
        if truck_weights[0]+bridge_weight>weight:
            bridge.append(0)
        else:
            current = truck_weights.pop(0)
            bridge.append(current)
            bridge_weight+=current
        time+=1
    return time+bridge_length


