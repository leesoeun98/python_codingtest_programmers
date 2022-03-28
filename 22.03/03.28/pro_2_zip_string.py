"""
12분 소요, 스스로 풂
핵심 포인트
1. slicing 할 때 list comprehension이랑 if 같이 쓰기
2. list내에서 연속적으로 반복되는 문자열 세는 법 이해
"""
def solution(s):
    ans=int(1e9)
    for unit in range(1, len(s)+1):
        sliced=[s[i*unit:(i+1)*unit] for i in range((len(s)//unit)+1) if s[i*unit:(i+1)*unit]!='']
        before=sliced[0]
        count=1
        res=""
        for i in range(1, len(sliced)):
            if before!=sliced[i]:
                if count!=1:
                    res+=str(count)+before
                else:
                    res+=before
                count=1
                before=sliced[i]
            else:
                count+=1
        if count!=1:
            res+=str(count)+before
        else:
            res+=before
        ans = min(ans, len(res))
    return ans