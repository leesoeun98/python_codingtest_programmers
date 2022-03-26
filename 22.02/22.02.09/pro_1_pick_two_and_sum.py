def solution(numbers):
    lst=[]
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i!=j and numbers[i]+numbers[j] not in lst:
                lst.append(numbers[i]+numbers[j])
    return sorted(lst)