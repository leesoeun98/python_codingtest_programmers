# 24:18 -
# 1231 이 stack에 순서대로 쌓여있을때만 햄버거 만듦 => list가 주어질때 만들 수 있는 햄버거 개수 int return
# 1차 시도 : 13분 소요, 혼자 풂 (정답인 것 같으나 시간 초과)

# 2차 시도 : find, join이 애초에 시간 초과 (30분 소요, 디른 사람 풀이 보고 이해함)
# => list에서 1일때만 참색 시작 (바로 햄버거가 되면 idx가 증가하는 거고, 햄버거가 안되면 안에서 찾은 후 해당 4개 원소를 del 한 후 idx 안에서 다시 탐색)
# => 이렇게 하면 무한대로 되돌아오지 않아도, 한 방향으로만 탐색 끝낼 수 있음 (len(ingredient)-4 < idx 면 종료)
def solution(ingredient):
    answer, idx = 0, 0
    while idx < len(ingredient)-3:
        # 처음이 빵일때만 탐색 시작
        if ingredient[idx] == 1:
            # 빵 시작일때 해당 범위 내에서 1,2,3,1 있으면 계속 찾기 (continue, idx 조정)
            # 한 번 찾으면, 해당 4개 원소 지우고 + 1,2,3,1 지웠는데 앞에 1이 있었으면 햄버거 또 만들 수 있으니까 idx-3
            if ingredient[idx:idx+4] == [1,2,3,1]:
                del ingredient[idx:idx+4]
                idx -= 3
                answer += 1
                continue
        idx += 1

    return answer
