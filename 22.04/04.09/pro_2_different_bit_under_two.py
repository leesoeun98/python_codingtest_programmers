"""
11분 소요, 스스로 풂
핵심 포인트
1. 짝수, 0일때는 +1 반환
2. 홀수면 딱 2비트만 바뀌도록 뒤부터 봤을때 가장먼저 0이 나오는 순간에 10000..를 더함
"""
def solution(numbers):
    res=[]
    for num in numbers:
        bin_num = bin(int(num))[2:]
        if bin_num[-2:]=="00" or bin_num[-2:]=="10" or num==0:
            res.append(num+1)
        else:
            idx=0
            for b in bin_num[::-1]:
                if b=="1":
                    idx+=1
                else:
                    break
            res.append(num+2**(idx-1))
    return res
