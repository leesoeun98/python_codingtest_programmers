def solution(s, n):
    final=""
    for a in s:
        if a.islower():
            final+=chr(97+(ord(a)-97+n)%26)
        elif a.isupper():
            final+=chr(65+(ord(a)-65+n)%26)
        else:
            final+=a
    return final