"""
4분 소요, 스스로 풂 (근데 외우다 싶히 한 문제라...ㅠㅠ)
핵심 포인트
1. number의 각 n과 stack의 [-1] 비교해서 작은 숫자면 제거
2. 아니면 stack에 append
3. k 만큼 제거가 다 안된거면 뒤에 k개만큼 제거하기
"""
def solution(number, k):
    stack=[]
    for n in number:
        while stack and stack[-1]<n and k>0:
            stack.pop()
            k-=1
        stack.append(n)
    return ''.join(stack) if k==0 else ''.join(stack[:-k])