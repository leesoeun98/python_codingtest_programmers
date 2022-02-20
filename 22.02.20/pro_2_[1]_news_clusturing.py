import re
def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()

    def making_set(strings):
        lst=[]
        for i in range(len(strings)):
            str = strings[i:i + 2]
            if len(re.findall(r'[^a-z]', str)) == 0 and len(str)>1:
                lst.append(str)
        return lst

    set1, set2=making_set(str1), making_set(str2)
    union, intersection, temp1, temp2=set1.copy(), [], set1.copy(), set1.copy()
    for s in set2:
        if s not in temp1:
            union.append(s)
        else:
            temp1.remove(s)
        if s in temp2:
            temp2.remove(s)
            intersection.append(s)
    return 65536 if len(set1)==0 and len(set2)==0 else int((len(intersection)/len(union))*65536)
