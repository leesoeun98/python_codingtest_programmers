"""
5분 소요, 스스로 풂
핵심 포인트
1. 각 자릿수 비교해서 전 숫자보다 큰 애들만 남길 것 => stack써서 큰 애들만 저장하자
2. n이 stack[-1]보다 작을동안 계속 제거
3. 아니면 stack.append(n)
4. k가 다 소진이 안됐으면 stack의 원소중 끝에 k만큼 제거하기
"""
def solution(number, k):
    stack=[]
    for n in number:
        while k>0 and len(stack)>0 and stack[-1]<n:
            stack.pop()
            k-=1
        stack.append(n)
    return ''.join(stack) if k==0 else ''.join(stack[:-k])
