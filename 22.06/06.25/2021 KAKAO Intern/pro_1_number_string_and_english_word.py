"""
3분 소요, 스스로 풂
핵심 포인트: replace 쓰기, dict 쓰기
"""
def solution(s):
    dic={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for num in dic.keys():
        s = s.replace(num, str(dic[num]))
    return int(s)