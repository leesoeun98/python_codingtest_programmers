"""
20분 정도 걸렸으나 다른 사람 해설 봄..
=>
1. 각 type별로 입을 수 있는 옷이 name 개수+1만큼 있음.
2. 1의 값을 type별로 곱하면 됨
3. 단, 아무것도 안 입은건 제외하므로 -1
"""
def solution(clothes):
    dict={}
    for name, type in clothes:
        if type not in dict:
            dict[type]=[]
        dict[type].append(name)
    total=1
    for key in dict.keys():
        total*=(len(dict[key])+1)
    return total-1