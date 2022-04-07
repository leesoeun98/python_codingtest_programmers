"""
4분 소요, 스스로 풂 (예전 코드 기억남)
1. 문자열 길이 만큼 곱해서 비교하기
2. 헷갈리지 말기 sorted는 반환값이 있음
3. str상태 숫자 정렬과 int일때 숫자 정렬 다름
"""
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))