def solution(s):
    if "-" in s:
        return -int("".join(s[1:]))
    elif "+" in s:
        return int("".join(s[1:]))
    else:
        return int("".join(s))