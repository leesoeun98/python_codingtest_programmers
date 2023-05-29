# 1차 성공: 13분 소요, 혼자 풂
# 2차 개선: intersection 대신 index
# 신고 횟수는 user 별로 1회씩만 처리됨 (여러번 신고해도 1번으로 처리)
# k번 이상 신고되면 정지, 해당 유저를 신고한 모든 유저에게 메일 발송 => user별로 처리 결과 받은 메일 횟수 배열에 담아 return

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # key: user value: user별로 신고당한 횟수
    user_reported_dict = {id: 0 for id in id_list}

    # user별로 신고당한 횟수 계산
    for row in set(report):
        user_reported_dict[row.split()[1]] += 1

    # 신고한 user별로 신고당한 횟수가 k 이상인 사람마다 +1
    # index로 answer랑 id_list 매핑
    for row in set(report):
        if user_reported_dict[row.split()[1]] >= k:
            answer[id_list.index(row.split()[0])] += 1

    return answer
