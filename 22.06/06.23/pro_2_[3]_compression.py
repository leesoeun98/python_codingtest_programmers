"""
1시간 10분 가량 소요, 다른 사람 코드 봄
구현력 문제 
"""

def solution(msg):
    lst = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    ans, idx, s = [], 0, msg[0]
    while idx != len(msg):
        if s in lst:
            if idx != len(msg) - 1:
                idx += 1
            else:
                ans.append(lst.index(s) + 1)
                break
            s += msg[idx]
        else:
            lst.append(s)
            ans.append(lst.index(s[:-1]) + 1)
            s = msg[idx]
    return ans
