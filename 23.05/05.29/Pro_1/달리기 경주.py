# 13:32 -
# 1차 시도 : 배열에 있는 원소로 다 swap하기 (정렬 문제) => 시간 초과
# 2차 시도 : 이름 별 idx (hash 사용)

# 바로 앞 선수 추월 시, 추월한 사람 이름 부름
# 현 순서 이름 배열, 이름 부른 배열 줄 때, 선수 등수 순 이름 배열 반환하기
result = dict()


def solution(players, callings):
    for idx, player in enumerate(players):
        result[player] = idx

    for calling in callings:
        target = [name for name, rank in result.items() if rank == result[calling] - 1][0]
        result[calling] -= 1
        result[target] += 1
    answer = dict(sorted(result.items(), key=lambda item: item[1]))
    return list(answer.keys())