"""
def solution(s):
    return len(list(filter(lambda x: x == "P" or x == "p", s))) == len(list(filter(lambda x: x == "Y" or x == "y", s)))
"""

def solution(s):
    return s.lower().count('p')==s.lower().count('y')