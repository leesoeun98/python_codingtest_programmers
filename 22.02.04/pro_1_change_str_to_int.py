def solution(s):
    if s.contains("-"):
        return int(-s.join(""))
    else:
        return int(s.join(""))