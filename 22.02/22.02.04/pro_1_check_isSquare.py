import math
def solution(x):
    return math.pow(math.sqrt(x)+1, 2) if math.sqrt(x).is_integer() else -1