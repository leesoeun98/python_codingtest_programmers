# 16분 소요, 혼자서 풂 (단, datetime은 검색 함)

# 모든 달이 28일까지 있을 때, today 기준 파기해야 할 privacies의 개인정보 번호 반환
# today는 YYYY.MM.DD / terms는 약관종류 (A-Z) 유효기간 (1-100)/ privacies는 날짜 (수집된 날짜) 약관종류
from datetime import datetime
from dateutil.relativedelta import relativedelta


def solution(today, terms, privacies):
    answer, terms_dict = [], dict()

    # today, terms 기준 term 별로 파기될 privacy 수집된 날짜 계산
    for term in terms:
        term_type, term_month = term.split(' ')
        terms_dict[term_type] = (datetime.strptime(today, '%Y.%m.%d') - relativedelta(months=int(term_month)))

    for idx, privacy in enumerate(privacies):
        collected, term = privacy.split(' ')
        collected_date = datetime(int(collected.split('.')[0]), int(collected.split('.')[1]),
                                  int(collected.split('.')[2]))
        if collected_date <= terms_dict[term]:
            answer.append(idx + 1)
    return answer
