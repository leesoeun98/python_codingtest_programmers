"""
5분 소요, 스스로 풂
<핵심 포인ㅌ>
1. dfs 이용 => dfs는 return 조건과 depth를 꼭 필수로 지정해야함
여기선 return 조건이 depth==len(number)이면서 result==target일때
반복하는 경우는 numbers의 모든 애들이 +, - 두 가지로 동작해야하므로 dfs를 두 번 시행
* nonlocal, global 주의
"""

def solution(numbers, target):
    count=0
    def dfs(result, depth):
        nonlocal count
        if depth==len(numbers):
            if result==target:
                count+=1
            return
        else:
            dfs(result+numbers[depth], depth+1)
            dfs(result-numbers[depth], depth+1)
    dfs(0,0)
    return count