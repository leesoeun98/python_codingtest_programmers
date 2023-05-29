# 1차 성공 : 36분 소요, 혼자 풂
# park, routes에 따라 강아지가 마지막으로 위치할 좌표 반환
# 주의하자! 가는 길목에 장애물이 있으면 못가는거임
direction_dict = {"E": [0, 1], "S": [1, 0], "W": [0, -1], "N": [-1, 0]}


def solution(park, routes):
    current_map = []
    # 시작점 찾고 current_map에 append
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                current_map.append([i, j])
    # 주어진 routes의 요소마다 반복
    for route in routes:
        direction, distance = route[0], int(route[2:])
        # 현 좌표
        current_x, current_y = current_map[-1]
        # 다음 좌표
        next_x, next_y = current_x + direction_dict[direction][0] * distance, current_y + direction_dict[direction][
            1] * distance
        # 현 좌표부터 다음 좌표까지 경로 찾고
        moving_route = ""
        for i in range(min(current_x, next_x), max(current_x, next_x) + 1):
            for j in range(min(current_y, next_y), max(current_y, next_y) + 1):
                moving_route += park[i][j] if 0 <= i < len(park) and 0 <= j < len(park[0]) else ""
        # 이동 경로에 X 포함되거나 park 범위 벗어나면 무시
        if 0 <= next_x < len(park) and 0 <= next_y < len(park[0]) and "X" not in moving_route:
            current_map.append([next_x, next_y])
    return current_map[-1]
