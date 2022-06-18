"""
14분 소요, 스스로 풂
핵심 포인트
1. 규칙 찾기
=> 1. 마지막이 0으로 끝나면 +1
=> 아니면 중간에 01로 되는 부분에서 +2**(idx-1)하면 됨
단, 맨 앞에 0 붙여줘서 2나 7같이 1, 111로만 나오고 0 이 없는 숫자들 예외처리 해주기
"""


def solution(numbers):
    ans = []
    for num in numbers:
        s = bin(int(num))[2:]
        bin_s = '0' + s
        if bin_s[-1] == '0':
            ans.append(num + 1)
        else:
            for idx, n in enumerate(bin_s[::-1]):
                if n == '0':
                    ans.append(num + 2 ** (idx - 1))
                    break
    return ans

