"""
45분 보다가 도저히 테스트케이스 2번 통과가 안돼서 다른 사람 풀이 참고
=> 그래도 40분 이상 추가 더 걸림
=> 12:14 재시도 10분 소요, 스스로 풂
핵심 포인트
1. 트럭 있는동안 다리 길이 유지하기 위해 매번 bridge.pop(0) 하고 weight상황에 따라 append
2. 트럭이 안남아 있으면 마지막 트럭이 다리 위에 있는거니까 트럭의 이동시간==다리 길이 만큼 더해서 return
3. 매번 sum하면 시간복잡도가 9000ms까지 걸리므로 bridge_weight 변수하나 둬서 실행하기 이 경우 220ms로 줆
"""
def solution(bridge_length, weight, truck_weights):
    bridge=[0 for _ in range(bridge_length)]
    time=0
    bridge_weight=0
    #bridge 길이는 계속 유지
    while True:
        # 트럭이 있으면 다리 길이 유지하면서 매번 bridge맨 앞 원소 빼고, 맨 뒤에 트럭이나 0 넣으면서 다리 길이 유지
        # 이때 time+=1로 트럭이 한 칸씩 이동
        if truck_weights:
            time+=1
            bridge_weight-=bridge[0]
            bridge.pop(0)
            if bridge_weight+truck_weights[0]<=weight:
                bridge_weight+=truck_weights[0]
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
        # 트럭 다 소진됐으면, 다리에는 마지막 트럭만 있으므로 해당 트럭이 이동해야하는 bridge_length만큼 더해서 반환
        else:
            return time + bridge_length


"""
다른 사람 풀이 
def solution(bridge_length, weight, truck_weights):
    time=0
    bridge=[]
    bridge_weight=0
    for truck in truck_weights:
        #truck마다 걸리는 time을 잼
        time+=1
        # bridge맨 앞 트럭이 올라가기 까지 걸린 시간 + 이동 시간이 time이랑 같으면 해당 트럭 bridge에서 빼기 (즉, 다리 다 건너면 빼는 것)
        if bridge and time == bridge[0][1]+bridge_length:
            bridge_weight-=bridge[0][0]
            bridge.pop(0)
        # 얘는 무게가 넘치면 빼는 것
        while bridge and bridge_weight+truck>weight:
            time = bridge[0][1]+bridge_length
            bridge_weight-=bridge[0][0]
            bridge.pop(0)
        #bridge에 올릴 수 있으면 truck 올림
        bridge_weight+=truck
        bridge.append([truck, time])
        print(bridge)
    #bridge에 올라간 마지막 트럭의 time(그 트럭이 올라가기까지 걸린 시간) + 해당 트럭이 이동하는데 걸리는 시간
    return bridge[-1][1]+bridge_length

"""
