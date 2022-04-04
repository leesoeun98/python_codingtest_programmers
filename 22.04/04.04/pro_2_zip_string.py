"""
12분 소요, 스스로 풂
핵심 포인트
1. sliced 배열 구성할 때 s[i*unit:(i+1)*unit]임에 주의
2. 연속된 문자열에서 같은 문자열 개수 세는 법 숙지
3. 변수 이름 주의 (예약어 쓰지 못함)
"""
def solution(s):
    ans=[]
    for unit in range(1, len(s)+1):
        sliced = [s[i*unit:(i+1)*unit] for i in range(len(s)+1) if s[i*unit:(i+1)*unit]!=""]
        before, count, string = sliced[0], 1, ""
        for i in range(1, len(sliced)):
            if before!=sliced[i]:
                if count==1:
                    string+=before
                elif count>1:
                    string+=str(count)+before
                before=sliced[i]
                count=1
            else:
                count+=1
        if count == 1:
            string += before
        else:
            string += str(count) + before
        ans.append(len(string))
    return min(ans)
