"""
20분 소요, 예전 코드봄
핵심 포인트
1. re로 문자열 list comprehension으로 구하는 법 list(re.findall())하는거 잊지 말기
2. count 구하는거 -  sum([max(count1, count2)])이런 형식임을 문제에서 착안함
"""
import re
def makingSet(string):
    string= string.lower()
    return [string[i:i + 2]for i in range(len(string)) if(len(list(re.findall('[a-z]', string[i:i + 2]))))==2]
def solution(str1, str2):
    lst1, lst2 = makingSet(str1), makingSet(str2)
    set1, set2 = set(lst1), set(lst2)

    intersection = set1 & set2
    union = set1 | set2

    intersection_count = sum([min(lst1.count(item),lst2.count(item))for item in intersection])
    union_count = sum([max(lst1.count(item),lst2.count(item))for item in union])

    return int(intersection_count/union_count*65536) if union_count!=0 else 65536