"""
내 이전 코드 봄

숫자 정렬
1. int: 정말 말 그대로 숫자 순
2. str: 앞부터 순서대로 비교 '9'>'34'
=> 이 문제 핵심은 각 원소가 1000보다 작으므로 *3으로 해서 앞부터 순서대로 비교해야 함
예) 9, 991 이면 999 991991991 로 9가 더 앞에 정렬됨 (9991) (9919보다 9991이 더 큼)
"""
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))