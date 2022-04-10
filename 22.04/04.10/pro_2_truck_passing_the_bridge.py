"""
8분 소요, 스스로 풂
핵심 포인트
1. 다리를 직접 만들고, 매번 pop(0)을 하고 append하기
2. 마지막 truck이 올랐으면 duration+bridge_length
3. 시간 초과 방지하기 위해 bridge_weight 변수 두기
"""
def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length
    bridge_weight=0
    duration=0
    while truck_weights:
        cur = bridge.pop(0)
        bridge_weight-=cur
        if bridge_weight+truck_weights[0]<=weight:
            truck = truck_weights.pop(0)
            bridge_weight+=truck
            bridge.append(truck)
        else:
            bridge.append(0)
        duration+=1
    return duration+bridge_length


