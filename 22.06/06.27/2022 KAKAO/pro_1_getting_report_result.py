"""
20분 소요, 스스로 풂
핵심 포인트
1. DB처럼 신고한 id, 당한 횟수, 차단된 user id set 구하기
2. 차단된 user id & 신고한 user id len 반환
"""


def solution(id_list, report, k):
    # user_dic은 user별 신고한 id 저장
    # ban_dic은 user별 신고당한 횟수
    # ban_lst는 차단된 user id
    user_dic, ban_dic, ban_lst = {}, {}, set()

    for user in id_list:
        user_dic[user] = set()
        ban_dic[user] = 0

    for repo in report:
        user, ban = repo.split(' ')
        user_dic[user].add(ban)

    for user, ban_set in user_dic.items():
        for ban in ban_set:
            ban_dic[ban] += 1
            if ban_dic[ban] >= k:
                ban_lst.add(ban)
    return [len(list(value & ban_lst)) for key, value in user_dic.items()]
