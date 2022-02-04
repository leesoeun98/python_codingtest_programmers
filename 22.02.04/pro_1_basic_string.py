"""def solution(s):
    if len(s)==4 or len(s)==6:
        if s.isdigit():
            return True
    return False
"""
def solution(s):
    return (len(s)==4 or len(s)==6) and s.isdigit()