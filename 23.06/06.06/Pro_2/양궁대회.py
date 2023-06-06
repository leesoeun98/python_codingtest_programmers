# 1시간 30분, 1차 성공 (단, 이전 풀이 그대로 봄)

# 어피치가 n발 다 쏜 후 라이언이 n발 쏨 
# => 각 발에 대해 k점을 어피치가 a발 라이언이 b발이면 max(a, b)인 사람이 k점 / a=b>0면 어피치가 k점(0-10) / a=b=0이면 둘다 0
# 최종 점수 더 높은 사람이 우승 (단, 같으면 어피치가 우승)
# 어피치가 n발 다 쏜 후 가장 큰 점수차로 이기기 위해 라이언이 n발(1-10)을 어떤 점수여야 하는지 return (단, 우승할 수 없으면 [-1])
# => 헷갈리지 말자 sum(info)=n이고, 우리가 반환할거는 각 점수당 몇발 쏘아야 하는지임 (즉, 반환 배열은 0-10점까지 총 11개로 길이 고정) +
# return 규칙 :
# 1. 10점부터 0점까지 순서대로 정수 배열에 담아 return
# 2. 라이언 우승 경우가 여러 가지 일 경우, 가장 낮은 점수를 더 많이 맞힌 경우를 return
import copy


def solution(n, info):
    # 가짓수: 2^11 => dfs (점수 먹고 / 안먹고 2가지를 11번)
    answer, gap = [], 0

    # 점수 계산 함수
    # 각 lst 원소 점수는 10부터 시작
    def calc(apeach_lst, lion_lst):
        apeach_score, lion_score = 0, 0
        for i in range(11):
            if apeach_lst[i] == lion_lst[i] == 0:
                continue
            if apeach_lst[i] >= lion_lst[i]:
                apeach_score += (10 - i)
            else:
                lion_score += (10 - i)
        return lion_score - apeach_score

    # 점수 먹거나, 안먹거나 (큰 점수부터 시작함)
    def dfs(idx, lion_lst, left_shots):
        nonlocal info, answer, gap
        # idx가 끝일때
        if idx == 11:
            # left_shots 남으면 0점에 몰빵 (lion 점수 낮을수록 좋음)
            if left_shots > 0:
                lion_lst[10] = left_shots
            # 점수 계산 후 lion이 더 크고 gap도 최대면 저장
            score_diff = calc(info, lion_lst)
            if score_diff > 0 and score_diff > gap:
                gap = score_diff
                answer = [copy.deepcopy(lion_lst)]
            if score_diff > 0 and score_diff == gap:
                answer.append(copy.deepcopy(lion_lst))
            return

        # 점수 먹으면
        if info[idx] < left_shots:
            lion_lst.append(info[idx] + 1)
            dfs(idx + 1, lion_lst, left_shots - info[idx] - 1)
            lion_lst.pop()

        # 점수 안먹으면
        lion_lst.append(0)
        dfs(idx + 1, lion_lst, left_shots)
        lion_lst.pop()

    dfs(0, [], n)
    # 가장 점수가 작은거부터 sort (각 원소를 거꾸로 정렬한것의 오름차순으로 정렬하면 첫번째 원소가 정답)
    answer.sort(key=lambda x: x[::-1], reverse=True)
    return [-1] if answer == [] else answer[0]
