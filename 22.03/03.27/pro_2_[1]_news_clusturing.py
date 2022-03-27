"""
10:20
"""
"""
35분 소요, 다른 사람 풀이 (다중집합의 교집합, 합집합 구하는 부분 봄)
핵심 포인트
1. 합집합 = 리스트1+리스트2-교집합
2. 단, 교집합 구할때 remove하는 경우 copy를 이용해야 함!!!
"""

"""
참고 하기 좋은 코드 (교 합 구하는 부분)
* 문제 잘 읽기.. 반환값 조건 다 틀려서 오래 걸림 + 교, 합 헷갈려서 오래 걸림
"""
import re


def solution(str1, str2):
    def split(string):
        lst = []
        string = string.lower()
        for i in range(len(string) - 1):
            if len(re.findall("[a-z]", string[i:i + 2])) == 2:
                lst.append(''.join(string[i:i + 2]))
        return lst
    list1, list2 = split(str1), split(str2)
    unite, intersection = set(list1) | set(list2), set(list1) & set(list2)
    # 합집합의 각 item이 list1, list2에 몇번 등장하는지 세서 모두 합함 (다중집합의 합집합)
    unite_sum = sum([max(list1.count(item), list2.count(item))for item in unite])
    inter_sum = sum([min(list1.count(item), list2.count(item))for item in intersection])
    return int(65536*(inter_sum/unite_sum)) if unite_sum!=0 else 65536
"""import re
def solution(str1, str2):
    def split(string):
        lst = []
        string = string.lower()
        for i in range(len(string) - 1):
            if len(re.findall("[a-z]", string[i:i + 2])) == 2:
                lst.append(''.join(string[i:i + 2]))
        return lst
    def intersection(lst1, lst2):
        result = []
        temp1= lst1.copy()
        for item in lst2:
            if item in temp1:
                result.append(item)
                temp1.remove(item)
        return result
    list1, list2 = split(str1), split(str2)
    un=list1+list2
    inter = intersection(list1, list2)
    for item in inter:
        if item in un:
            un.remove(item)
    return 65536 * (len(intersection(list1, list2))) // len(un) if len(
        un) != 0 else 65536
"""