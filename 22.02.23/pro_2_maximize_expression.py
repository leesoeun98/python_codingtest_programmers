"""
1시간 6분 걸림 + 다른 사람 풀이도 봄
<주의사항>
1. regex
2. 문제 접근법 => 연산자 3종류이므로 6가지 경우 모두 해야함.
우선순위를 애초에 list로 주고서, operation에 연산자가 있으면 계산하게 하고, 피연산자 2개랑 연산자 1개 없애면 됨
3. eval 함수 쓰기
"""
import re
def solution(expression):
    priors = [['*','+','-'],['*','-','+'],['-','+','*'],['-','*','+'],['+','*','-'],['+','-','*']]
    ans=[]
    for prior in priors:
        numbers = re.split('[+*-]', expression)
        operation = list(filter(lambda x: len(x) == 1, re.split('[0-9]', expression)))
        for op in prior:
            while op in operation:
                idx = operation.index(op)
                numbers[idx] = str(eval(numbers[idx]+op+numbers[idx+1]))
                del numbers[idx+1]
                del operation[idx]
        ans.append(abs(int(numbers[0])))
    return max(ans)
