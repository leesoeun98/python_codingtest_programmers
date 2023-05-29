# 13:32 -
# 바로 앞 선수 추월 시, 추월한 사람 이름 부름
# 현 순서 이름 배열, 이름 부른 배열 줄 때, 선수 등수 순 이름 배열 반환하기
def solution(players, callings):
    for calling in callings:
        idx = players.index(calling)
        players[idx] = players[idx-1]
        players[idx-1]=calling
    return players