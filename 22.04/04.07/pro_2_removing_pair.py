"""
1분소요, 스스로 풀었으나 예전에 stack쓴거 기억함 ㅠㅠ
핵심 포인트
1. stack으로 이전 문자열을 저장, 이전문자열과 현 문자열 비교하자
=> 같으면 pop하고 아예 append 안해서 문자 2개 없애기
"""
def solution(s):
    stack=[]
    for alphabet in s:
        if stack and stack[-1]==alphabet:
            stack.pop()
        else:
            stack.append(alphabet)
    return 1 if len(stack)==0 else 0