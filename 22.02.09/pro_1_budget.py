def solution(d, budget):
    d.sort()
    count=0
    for b in d:
        if b<=budget:
            budget-=b
            count+=1
    return count