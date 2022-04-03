"""
4분 소요, 스스로 풀었으나 옛날 코드 기억해서 풂..ㅜㅜ
핵심 포인트
1. sorted시 lambda로 각 numbers*3으로 같은 길이로 만들어서 비교, 단, 내림차순이어야 하므로 reverse 걸기
2. 앞에 0오는거 없애기 위해 str(int())처리 하기
"""
def solution(numbers):
    numbers = map(str, numbers)
    numbers = sorted(numbers, key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))
