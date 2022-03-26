def solution(array, commands):
    lst=[]
    for command in commands:
        i,j,k=command
        lst.append(list(sorted(array[i-1:j]))[k-1])
    return lst
"""
i,j,k = 배열 이것도 생각하기 
"""