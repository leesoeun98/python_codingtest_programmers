def solution(n):
    return sum(list(filter(lambda i:n%i==0, range(1, n+1))))