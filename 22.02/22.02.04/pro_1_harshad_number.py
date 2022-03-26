"""
def solution(x):
    sumdigit=0
    target=x
    while target>0:
        sumdigit=sumdigit+target%10
        target=target//10
    if x%sumdigit==0:
        return True
    else:
        return False
"""

def solution(x):
    return x%sum([int(i) for i in str(x)])==0


print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))