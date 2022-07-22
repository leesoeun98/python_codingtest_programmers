"""
30분 소요, 스스로 풂 (단, 테스트케이스 힌트 받음)
핵심 포인트
1. 공백 유지가 관건 => re로 공백 포함해서 모두 단어 split한 후 단어.strip()만 대체해서 공백 유지하기
"""
import re

def solution(s):
    words, res = list(re.findall(r'[\s]*[0-9a-zA-Z]+[\s]*', s)), ""
    for word in words:
        newword = word.strip().lower()
        newword = newword[0].upper() + newword[1:]
        res += (word.replace(word.strip(), newword))
    return res

