# 1차 성공 : 11분 소요, 혼자 풂
# 마지막 좌표는 +1, +1임에 주의!
# wallpaper에서 (세로, 가로 좌표) 빈칸은 . 파일은 #
# 최소한의 거리를 갖는 드래그로 모든 파일을 선택해서 지우고 싶음
# 드래그는 S(lux, luy) => E(rdx, rdy) 이때의 거리는 |rdx-lux| + |rdy-luy|

# 각 파일을 좌표를 모두 구한 후, min(lux), min(luy), max(rdx), max(rdy) 찾기
file_location = []


def solution(wallpaper):
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                file_location.append([i, j])

    answer = [min([x for x, y in file_location]), min([y for x, y in file_location]),
              max([x for x, y in file_location]) + 1, max([y for x, y in file_location]) + 1]
    return answer
