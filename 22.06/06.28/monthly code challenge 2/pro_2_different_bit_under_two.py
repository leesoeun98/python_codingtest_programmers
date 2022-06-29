"""
8분 소요, 스스로 풂
핵심 포인트
1. 문제 이해 - 0, 1로 끝날때를 나눠서 처리
"""
def solution(numbers):
    answer = []
    for num in numbers:
        s = '0'+bin(int(num))[2:]
        # 0으로 끝날 때
        if s[-1]=='0':
            answer.append(num+1)
        # 1로 끝날 때
        else:
            idx=0
            for n in s[::-1]:
                if n=='0':
                    answer.append(num+2**(idx-1))
                    break
                idx+=1
    return answer