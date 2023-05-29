# 22분 소요, 3차 성공 (다른 사람 풀이 참고)
# 1차 시도 : 배열에 있는 원소로 다 swap하기 (정렬 문제) => 시간 초과
# 2차 시도 : 이름 별 idx (hash 사용) => target name 찾는데서 시간 초과 (그래도 좀 줄었음)
# 3차 시도 : hash, swap 같이 쓰기 => 성공 / 다른 사람 풀이 봄

# 바로 앞 선수 추월 시, 추월한 사람 이름 부름
# 현 순서 이름 배열, 이름 부른 배열 줄 때, 선수 등수 순 이름 배열 반환하기
rank_dict = dict()


def solution(players, callings):
    for idx, player in enumerate(players):
        rank_dict[player] = idx

    for calling in callings:
        pre_player_rank, post_player_rank = rank_dict[calling] - 1, rank_dict[calling]
        pre_player_name, post_player_name = players[pre_player_rank], players[post_player_rank]
        # dict 갱신
        rank_dict[pre_player_name], rank_dict[post_player_name] = post_player_rank, pre_player_rank
        # list 갱신
        players[pre_player_rank], players[post_player_rank] = players[post_player_rank], players[pre_player_rank]
    return players