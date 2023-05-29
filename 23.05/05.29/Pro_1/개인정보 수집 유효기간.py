# 16분 소요, 혼자서 풂 (단, datetime은 검색 함)
# 2차 개선 : 그냥 총 date 합으로 계산해서 datetime 쓰지 말자 (개선이 은근 오래걸림..365가 아니라 28일임에 주의하자)
# => map써서 코드 간단히 하자

# 모든 달이 28일까지 있을 때, today 기준 파기해야 할 privacies의 개인정보 번호 반환
# today는 YYYY.MM.DD / terms는 약관종류 (A-Z) 유효기간 (1-100)/ privacies는 날짜 (수집된 날짜) 약관종류

def make_date(date_str):
    year, month, date = map(int, date_str.split('.'))
    return year*28*12 + month*28 + date


def solution(today, terms, privacies):
    # today, terms 기준 term 별로 파기될 privacy 수집된 날짜 계산
    answer, terms_dict = [], {term[0]: int(term[2:])*28 for term in terms}
    today = make_date(today)

    for idx, privacy in enumerate(privacies):
        collected, term = privacy.split(' ')
        if make_date(collected) + terms_dict[term]<= today:
            answer.append(idx + 1)
    return answer
