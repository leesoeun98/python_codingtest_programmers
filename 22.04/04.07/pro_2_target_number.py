"""
6분 소요, 스스로 풂
핵심 포인트 - dfs로 depth, 종료 조건 확실히
꼭 기억하기
1. global: 전역변수로 def 밖에 변수 정의하고 함수에서 동일 이름 변수 쓸때 global 변수라고 지정하기
2. nonlocal: 한 단계 위의 함수 내 변수 쓰고 싶을때 안에 함수에서 nonlocal 이라고 쓰기
=> 이 경우 def solution의 count를 쓰기 위해 dfs에서 nonlocal count라고 명시함
"""
def solution(numbers, target):
    count = 0
    def dfs(depth, res):
        if depth==len(numbers):
            if res==target:
                nonlocal count
                count+=1
            return
        else:
            dfs(depth+1, res+numbers[depth])
            dfs(depth+1, res-numbers[depth])
    dfs(0,0)
    return count