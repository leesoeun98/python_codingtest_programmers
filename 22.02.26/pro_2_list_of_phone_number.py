"""
내 이전 코드 봄
이중 for문이면 당연히 효율성 통과 못함 => 문자열이므로 sort한 후, 바로 다음거가 전거를 포함하는지만 보면 됨
"""
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True