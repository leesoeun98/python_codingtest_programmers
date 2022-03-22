"""
15분 소요, 접근법부터 예전 코드 봄
<핵심 포인트>
1. 6가지 경우의 수 다 만들기
2. 각 ['*', '-', '+'] 경우에서 각 연산자 op에 대해, operator에 op가 다 사라질때까지 계산 (우선순위 부여)
3. eval 함수 쓰기, idx에 맞는 숫자랑 연산자 찾아서 계산 후 del 쓰기
"""
import re
def solution(expression):
    ans=[]
    priors = [['*', '-', '+'], ['*', '+', '-'], ['-', '+', '*'], ['-', '*', '+'], ['+', '-', '*'], ['+', '*', '-']]
    for prior in priors:
        operator = re.findall("[+*-]", expression)
        numbers = re.findall("\d+", expression)
        for op in prior:
            while op in operator:
                idx = operator.index(op)
                numbers[idx] = str(eval(numbers[idx]+op+numbers[idx+1]))
                del numbers[idx+1]
                del operator[idx]
        ans.append(abs(int(numbers[0])))
    return max(ans)


