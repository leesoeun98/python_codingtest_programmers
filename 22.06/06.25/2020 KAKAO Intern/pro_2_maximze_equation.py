"""
20분 소요, 이전 코드 봄
핵심 포인트
1. list[:]를 사용해서 pop해도 for문 다 돌기
2. insert, index, eval 활용하기
"""
priorities = [['*', '-', '+'], ['*', '+', '-'], ['-', '+', '*'], ['-', '*', '+'], ['+', '-', '*'], ['+', '*', '-']]
import re


def solution(expression):
    numbers = re.findall(r'\d+', expression)
    operators = re.findall(r'[-+*]', expression)
    ans = []
    for prior in priorities:
        copy_numbers, copy_operators = numbers.copy(), operators.copy()
        for target_operator in prior:
            for operator in copy_operators[:]:
                if operator == target_operator:
                    idx = copy_operators.index(operator)
                    copy_numbers.insert(idx,
                        str(eval(copy_numbers.pop(idx) + copy_operators.pop(idx) + copy_numbers.pop(idx))))
        ans.append(abs(int(copy_numbers[0])))
    return max(ans)