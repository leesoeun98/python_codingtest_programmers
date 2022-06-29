"""
3분 소요, 스스로 풂
"""


def solution(price, money, count):
    p=sum([price*i for i in range(1, count+1)])
    return 0 if p<money else p-money