"""
str sort는 불가, sorted는 가능
"""
def solution(s):
    return ''.join(sorted(s, reverse=True))