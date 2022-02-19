"""
stack 이용하는 문제 => 새로운 list에 문자를 담는데, list[-1]과 현 문자를 비교해서 이미 있다면 연속된것이므로 pop 아니면 append
"""
def solution(s):
    lst=[]
    for alpha in s:
        if len(lst)>0 and lst[-1]==alpha:
            lst.pop()
        else:
            lst.append(alpha)
    return 1 if len(lst)==0 else 0