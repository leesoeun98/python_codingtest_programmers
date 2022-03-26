def solution(arr, divisor):
    lst = []
    for element in arr:
        if element%divisor==0:
            lst.append(element)
    return sorted(lst) if len(lst)!=0 else [-1]