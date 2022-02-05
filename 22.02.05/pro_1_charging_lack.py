def solution(price, money, count):
    return max(0, sum(list(map(lambda x:price*x, range(1, count+1))))-money)