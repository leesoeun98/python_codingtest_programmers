"""
13분 소요, 예전 코드 봄
핵심 포인트
1. 문제에서 자카드 유사법 max, min 이용해서 구한거에서 방법 착안하기
2. unite_sum, intersection_sum 구하는 부분
3. regex로 문자열 뽑아내는 부분
"""
import re
def solution(str1, str2):
    def splitWord(string):
        lst=[]
        for i in range(len(string)):
            if len(list(re.findall("[a-z]", string[i:i + 2]))) == 2:
                lst.append(string[i:i + 2])
        return lst
    str1, str2= str1.lower(), str2.lower()
    list1, list2= splitWord(str1), splitWord(str2)
    unite = set(list1) | set(list2)
    intersection = set(list1) & set(list2)

    unite_sum = sum([max(list1.count(item), list2.count(item)) for item in unite])
    intersection_sum = sum([min(list1.count(item), list2.count(item))for item in intersection])
    return int(65536*intersection_sum/unite_sum) if unite_sum!=0 else 65536