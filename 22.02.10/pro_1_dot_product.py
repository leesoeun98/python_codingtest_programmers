def solution(a, b):
    return sum(list(f*s for f, s in zip(a, b)))

"""
zip 사용하기 => iterable한 데이터의 각 요소를 짝지어서 반환해줌 
"""