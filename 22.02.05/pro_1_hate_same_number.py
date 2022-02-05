"""def solution(arr):
    lst=[arr[0]]
    for i in range(1, len(arr)):
        if arr[i]!=arr[i-1]:
            lst.append(arr[i])
    return lst"""
def solution(arr):
    lst=[]
    for element in arr:
        if len(lst)==0 or lst[-1]!=element:
            lst.append(element)
    return lst