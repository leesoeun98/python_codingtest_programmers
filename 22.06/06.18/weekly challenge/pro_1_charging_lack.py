"""
2분소요, 스스로 풂 (모자라지 않으면 0 주는거에 주의)
"""
def solution(price, money, count):
    return 0 if sum([price*i for i in range(1, count+1)])-money < 0 else sum([price*i for i in range(1, count+1)])-money