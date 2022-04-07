"""
3분 소요, 스스로 풂
핵심 포인트
1. hash 하기 위해 dict 씀
2. dict key에 미리 번호 다 넣어놓고, 이중 for문으로 dic key에 있는지 확인
"""
def solution(phone_book):
    dic={}
    for idx, phone_number in enumerate(phone_book):
        dic[phone_number]=idx
    for number in phone_book:
        res=""
        for i in range(len(number)-1):
            res+=number[i]
            if res in dic:
                return False
    return True
