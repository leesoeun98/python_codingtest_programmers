"""
26분 소요, 예전 코드 봄
틀린 부분
1. makingSet 부분 (급하게 하지 말자)
=> 나머지 로직은 그래도 스스로 생각해 냄
"""
import re
def solution(str1, str2):
    def makingSet(string):
        string = string.lower()
        return [string[i:i + 2] for i in range(len(string)) if len(list(re.findall('[a-z]', string[i:i + 2]))) == 2]

    lst1, lst2 = makingSet(str1), makingSet(str2)

    union = set(lst1) | set(lst2)
    intersection = set(lst1) & set(lst2)

    union_count = sum([max(lst1.count(item), lst2.count(item)) for item in union])
    intersection_count = sum([min(lst1.count(item), lst2.count(item)) for item in intersection])

    return 65536 if union_count == 0 else int(intersection_count / union_count * 65536)
