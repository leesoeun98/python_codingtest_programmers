def solution(x):
    count=0
    while x!=1:
        if count>500:
            return -1
        if x%2==0:
            x/=2
            count+=1
        else:
            x=x*3+1
            count+=1
    return count


print(solution(626331))
print(solution(6))
print(solution(16))