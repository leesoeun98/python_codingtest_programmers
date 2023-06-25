# 10:56 - 11:50 1차 시도 실패 (시간 초과)

# n개 집에 배달, 빈 박스는 수거, 차있는 박스는 배달
# 트럭에는 상자를 최대 cap개 실을 수 있음
# 각 집마다 배달할 개수, 수거 개수를 알 때 트럭 1개로 모든 배달 및 수거를 마치고 돌아오는 최소 이동 거리 (단, 원하는 개수만큼만 수거, 배달 가능)

# 일단 끝에서부터 cap 개수에 맞게 수거 + 배달해서 돌아오는 순으로?
def solution(cap, n, deliveries, pickups):
    dist, truck_remain, house_idx = 0, cap, []

    while sum(deliveries) > 0 or sum(pickups) > 0:
        # 택배 싣고 배달 (편도 -> 방향)
        for i in range(n - 1, -1, -1):
            if truck_remain > 0 and deliveries[i]>0:
                house_idx.append(i)
                if deliveries[i] <= truck_remain:
                    truck_remain -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= truck_remain
                    truck_remain = 0
        truck_remain = cap
        # 택배 수거
        for i in range(n - 1, -1, -1):
            if truck_remain > 0 and pickups[i]>0:
                house_idx.append(i)
                if pickups[i] <= truck_remain:
                    truck_remain -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= truck_remain
                    truck_remain = 0
        truck_remain = cap
        # 편도 거리 더하기
        dist += (max(house_idx)+1) * 2
        house_idx = []
    return dist
