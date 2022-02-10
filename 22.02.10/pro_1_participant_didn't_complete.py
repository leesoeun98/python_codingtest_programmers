def solution(participant, completion):
    dic={}
    for p in participant:
        if p in dic:
            dic[p]+=1
        else:
            dic[p]=1
    for c in completion:
        if c in dic:
            dic[c]-=1
    return [k for k,v in dic.items() if v!=0][0]
