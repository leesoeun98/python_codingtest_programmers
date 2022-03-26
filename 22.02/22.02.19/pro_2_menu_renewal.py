from itertools import combinations
def solution(orders, course):
    lst=[]
    for c in course:
        dic={}
        for order in orders:
            for combi in list(set(combinations(order, c))):
                m = ''.join(sorted(combi))
                if m in dic:
                    dic[m]+=1
                else:
                    dic[m]=1
        sorted_menu = list(dict(filter(lambda elem: elem[1]>=max(dic.values()) and elem[1]>=2, dic.items())).keys())
        for menu in sorted_menu:
            lst.append(menu)
    return sorted(lst)