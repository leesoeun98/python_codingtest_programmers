def solution(numbers):
    return sum(list(filter(lambda x: x not in numbers,[0,1,2,3,4,5,6,7,8,9])))