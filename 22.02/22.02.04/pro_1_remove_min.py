def solution(lst):
    lst.remove(min(lst))
    return [-1] if len(lst)==0 else lst