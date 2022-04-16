"""
3분 소요, 스스로 풂 (근데 예전 코드 기억함 ㅜㅠ)
핵심 포인트
1. sorted에서 map으로 문자열로 만들고, lambda로 *3해서 비교, reverse = True로 내림차순
2. str(int())로 반환
"""
def solution(numbers):
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))