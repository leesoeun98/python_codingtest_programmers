"""
7분 소요, 스스로 풂 (테스트 케이스 참고함)
핵심 포인트
1. number의 각 n과 비교해 더 큰 애만 남기겠다.
2. k가 0이 안됐으면 뒷부분 다 날리기
"""
def solution(number, k):
    stack=[]
    for n in number:
        while stack and stack[-1]<n and k>0:
            stack.pop()
            k-=1
        stack.append(n)
    return ''.join(stack) if k==0 else ''.join(stack[:-k])
