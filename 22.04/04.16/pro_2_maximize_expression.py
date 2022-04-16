"""
19분소요, 스스로 풂 (그러나 반례 찾아봄)
핵심 포인트
1. 6가지 조합 priorities 만들어놓기
2. re로 operations, numbers 뽑아내고 매번 copy하기
3.         for priority_operation in priority:
            for operation_expression in operations_copy[:]:
                if priority_operation==operation_expression: 이걸로 priority에 있는 연산자부터 모두 실행
4. eval 쓰기, insert(idx, str(res)) 임에 주의
5. ans.append() 위치 주의
"""
priorities = [['*','+','-'], ['*','-','+'], ['-','*','+'], ['-','+','*'], ['+','-','*'], ['+','*','-']]
import re
def solution(expression):
    ans=[]
    numbers = list(re.findall('[0-9]+', expression))
    operations = list(re.findall('[+*-]', expression))
    for priority in priorities:
        numbers_copy, operations_copy = numbers.copy(), operations.copy()
        for priority_operation in priority:
            for operation_expression in operations_copy[:]:
                if priority_operation==operation_expression:
                    idx = operations_copy.index(operation_expression)
                    res = eval(str(numbers_copy.pop(idx))+operations_copy.pop(idx)+str(numbers_copy.pop(idx)))
                    numbers_copy.insert(idx, str(res))
        ans.append(abs(int(numbers_copy[0])))
    return max(ans)

print(solution("100-200*300-500+20"))