# 23분 소요, 1차 성공 (혼자서 풂)
# 시간, 공간복잡도 판단 후 for문 2중으로 써도 괜찮음 확인 => 중복순열 만든 후 2중 for문으로! 마지막엔 sort

# 가입자 수 증가 우선, 판매액 증가 2순위
# n명(1-100)에게 m개(1-7)를 팔되 이모티콘 각각 10, 20, 30, 40 할인율 중 택 1 => 4^7*100 = 2^14*100 = 1024 * 16 *100 = 1638400
# n명 각각 기준할인율 이상이면 모두 구매, 구매 합이 일정가격 이상이면 구매 취소 후 가입

from itertools import product


def solution(users, emoticons):
    discount_list, answer = [], []
    for p in product([10, 20, 30, 40], repeat=len(emoticons)):
        discount_list.append(p)

    for discount_rate in discount_list:
        enrollment_count, buy_cost = 0, 0
        for user_rate, user_cost in users:
            targets = [cost * (1 - rate / 100) for rate, cost in zip(discount_rate, emoticons) if rate >= user_rate]
            if sum(targets) >= user_cost:
                enrollment_count += 1
            else:
                buy_cost += sum(targets)
        answer.append([enrollment_count, buy_cost])
    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]


