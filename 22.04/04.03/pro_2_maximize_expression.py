"""
26분 소요, 스스로 풂
핵심 포인트
1. eval 쓰기
2. copy해야 함 (매번 pop을 하므로) // re로 숫자랑 연산자 뽑아내기
3. copy_operators[:]로 copy_operators매번 pop해서 달라져도 다 돌 수 있도록 하기
4. abs임에 주의하기
5. pop과 insert 시 idx 주의하기
"""
priorities = [['*','-','+'],['*','+','-'], ['-','+','*'],['-','*','+'],['+','*','-'],['+','-','*']]
import re
def solution(expression):
    ans=[]
    numbers = list(re.findall('[\d]+', expression))
    operators = list(re.findall('[+*-]',expression))
    #우선순위 종류별로 6번 반복
    for i in range(6):
        copy_operators=operators.copy()
        copy_numbers = numbers.copy()
        for prior in priorities[i]:
            for operator in copy_operators[:]:
                if operator==prior:
                    idx = copy_operators.index(operator)
                    operator = copy_operators.pop(idx)
                    if len(copy_numbers)>1:
                        f, s = copy_numbers.pop(idx), copy_numbers.pop(idx)
                        copy_numbers.insert(idx, str(eval(f+operator+s)))
        ans.append(abs(int(copy_numbers[0])))
    return max(ans)