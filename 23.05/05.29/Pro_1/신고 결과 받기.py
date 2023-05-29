# 1차 성공: 13분 소요, 혼자 풂
# 신고 횟수는 user 별로 1회씩만 처리됨 (여러번 신고해도 1번으로 처리)
# k번 이상 신고되면 정지, 해당 유저를 신고한 모든 유저에게 메일 발송 => user별로 처리 결과 받은 메일 횟수 배열에 담아 return

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def solution(id_list, report, k):
    # key: user value: user별로 신고한 상대 id 목록
    user_report_dict = {id: set() for id in id_list}
    # key: user value: user별로 신고당한 횟수
    user_reported_dict = {id: 0 for id in id_list}

    for row in report:
        user, reported_user = row.split(' ')
        user_report_dict[user].add(reported_user)

    for value in user_report_dict.values():
        for id in value:
            user_reported_dict[id] += 1

    suspended_user = [id for id, count in user_reported_dict.items() if count >= k]
    answer = [len(intersection(reported_list, suspended_user)) for id, reported_list in user_report_dict.items()]
    return answer


