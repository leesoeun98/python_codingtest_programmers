# 1차 성공 : 17분 소요
# survey, choices를 바탕으로 mbti 16가지 조합 중 한 개 반환하기

# 1, 7 => 3점 / 2, 6 => 2점 / 3, 5 => 1 / 4 => 0점
# AN => 비동의면 A, 동의면 N (즉, 123을 고르면 A / 567을 고르면 N)
# 높은 점수 받은것이 결과이며, 같은 점수면 알파벳 사전 순으로 결정
mbti = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}


def solution(survey, choices):
    answer = ""
    for question, choice in zip(survey, choices):
        if choice < 4:
            mbti[question[0]] += 4 - choice
        elif choice > 4:
            mbti[question[1]] += choice - 4
    for types in ["RT", "CF", "JM", "AN"]:
        answer += types[0] if mbti[types[0]] >= mbti[types[1]] else types[1]
    return answer
