# 30분 소요, 스스로 풂 (1차 통과)
# 너무 오랜만이라 문자열 처리에 약해짐 >> 문자열 처리는 Regex 쓰자
# 문제 잘 읽자
import re


def solution(s):
    answer, splitted = '', re.findall("\s+|[0-9a-zA-Z]+", s)

    for word in splitted:
        if word[0].isalpha():
            answer += word[0].upper() + word[1:].lower()
        elif word[0].isdigit():
            answer += word[0] + word[1:].lower()
        else:
            answer += word

    return answer