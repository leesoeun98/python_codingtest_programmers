"""
18분 소요, 스스로 풂
핵심 포인트
1. 트럭은 순서대로 건너야 하고, 1초에 1만큼 이동함
2. bridge를 아예 만들어서 매번 pop(0)하고 truck이나 0을 append해서 bridge길이 유지
3. truck이 더 이상 없으면 bridge pop만 해서 time+=1
4. 단, truck이 bridge에 못 올라가면 insert(0,truck)으로 truck 순서 유지
"""
def solution(bridge_length, weight, truck_weights):
    bridge=[0]*bridge_length
    bridge_weight = 0
    time=0
    while bridge:
        bridge_weight -= bridge.pop(0)
        if truck_weights:
            truck = truck_weights.pop(0)
            if bridge_weight+truck<=weight:
                bridge.append(truck)
                bridge_weight+=truck
            elif bridge_weight+truck>weight:
                bridge.append(0)
                truck_weights.insert(0, truck)
        time+=1
    return time



