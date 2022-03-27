"""
4분 소요, 이전 코드 참고함
핵심 포인트: numbers의 각 원소가 세자리이므로, *3해서 비교하기
"""
def solution(numbers):
    strNum = sorted(list(map(str, numbers)), key = lambda x: x*3, reverse=True)
    return str(int(''.join(strNum)))
