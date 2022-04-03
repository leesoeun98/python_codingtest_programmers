"""
3분 소요, 스스로 풀었으나 예전 코드 기억함..ㅠㅠ
핵심 포인트
1. in을 쓰면 안됨. 접두어인지 확인이니까 이전 문자열 길이만큼 앞에만 잘라서 같은지 비교해야 함
"""
"""def solution(phone_book):
    phone_book = sorted(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True"""
"""
dict쓰는 방법, 다른 사람 코드 참조함
1. phone_book의 item 자체를 dic key로 저장
2. phone_book의 item을 앞에서부터 한글자씩 잘라 봤을 때, 해당 자른 글자가 dict에 있단건 접두어니까 바로 return 
3. 단, 자기 자신이 들어가는걸 방지하기 위해 range(1, len(number))로 마지막 한글자 제외해서 찾기
"""
def solution(phone_book):
    dic={}
    for idx, number in enumerate(phone_book):
        dic[number] = idx
    for number in phone_book:
        for i in range(1, len(number)):
            if number[:i] in dic:
                return False
    return True

