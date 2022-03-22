"""
10분 소요, 예전 코드 봄
<핵심 포인트>
1. '접두사'인지 확인해야 하기 때문에 in을 쓰는게 아니라 slicing으로 직접 == 으로 비교해야 함
2. sorting후 앞뒤만 확인하면 됨
"""
def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        if phone_book[i-1]==phone_book[i][:len(phone_book[i-1])]:
            return False
    return True
"""
hash 사용 법 (근데 틀림...그리고 다른 풀이도 없음..)
"""
"""def solution(phone_book):
    dict={}
    for number in set(phone_book):
        for i in range(1, len(number)+1):
            if number[:i] not in dict:
                dict[number[:i]]=1
            else:
                dict[number[:i]]+=1
    print(dict)
    return False if len(list(filter(lambda x: x[1]>1, dict.items())))>1 else True"""

