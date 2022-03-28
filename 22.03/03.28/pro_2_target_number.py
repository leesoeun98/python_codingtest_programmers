"""
4분 소요, nonlocal 에서 예전 코드 참고
=> 그냥 애매하면 count 변수를 함수 밖으로 빼자...
핵심 포인트
1. +, - 두 갈래니까 dfs 두번 호출, depth랑 res 변수가 인자로 필수
2. dfs 종료 조건문 필수로 넣기 
"""
def solution(numbers, target):
    count=0
    def dfs(depth, res):
        nonlocal count
        if depth==len(numbers):
            if target==res:
                count+=1
        else:
            dfs(depth+1, res+numbers[depth])
            dfs(depth+1, res-numbers[depth])
    dfs(0,0)
    return count
