"""
9분 소요, 스스로 풂
핵심 포인트
1. 문자열 unit 별로 자르기 : list comprehension 사용
2. 문자열 내에서 같은 문자열 개수 세기
3. len(res)를 append 해서 min값 찾기
"""
def solution(s):
    ans=[]
    for unit in range(1, len(s)+1):
        lst = [s[i*unit:(i+1)*unit] for i in range(len(s)) if s[i*unit:(i+1)*unit]!='']
        beforeStr, count, res = lst[0],1, ""
        for i in range(1, len(lst)):
            if beforeStr!=lst[i]:
                if count==1:
                    res+=beforeStr
                else:
                    res+=str(count)+beforeStr
                count=1
                beforeStr = lst[i]
            else:
                count+=1
        if count == 1:
            res += beforeStr
        else:
            res += str(count) + beforeStr
        ans.append(len(res))
    return min(ans)