"""
15분, 예전 코드 봄 (for operator in opertors_copy[:]:) 이부분
핵심 포인트
1. 6가지 우선순위 조합 만들고, 6번 돌되
2. 각 연산자 prior별로 operators_copy의 연산자 모두 돌아야 함 (pop되더라도)
-> 이를 위해선 [:] 써야 list가 변화가 있어도 list 다 돎
"""
priorites = [['*','-','+'],['*','+','-'],['-','+','*'],['-','*','+'],['+','-','*'],['+','*','-']]
import re
def solution(expression):
    operators = list(re.findall('[+*-]', expression))
    numbers = list(re.findall('\d+', expression))
    res=[]

    for i in range(6):
        opertors_copy= operators.copy()
        numbers_copy = numbers.copy()
        for prior in priorites[i]:
            for operator in opertors_copy[:]:
                if operator==prior:
                    idx = opertors_copy.index(operator)
                    opertors_copy.pop(idx)
                    f, s= numbers_copy.pop(idx), numbers_copy.pop(idx)
                    numbers_copy.insert(idx, str(eval(f+operator+s)))
        res.append(abs(int(numbers_copy[0])))
    return max(res)
