"""
30분 정도 걸림
<문제 접근 방식>
1. 1부터 len(s)까지 unit으로 문자열 자르기 (slicing)
2. string 내에서 반복 되는 부분 count 하기 (16-32줄)
"""
import math

def solution(s):
    ans=int(1e9)
    for i in range(1, len(s) + 1):
        sliced = []
        for j in range(math.ceil(len(s) / i)):
            # slicing에서 예전 코드 참고함..
            sliced.append(s[i * j:i * (j + 1)])
        count = 1
        result = ""
        before=sliced[0]
        for k in range(1, len(sliced)):
            if before != sliced[k]:
                if count > 1:
                    result += (str(count) + before)
                else:
                    result += before
                count = 1
                before=sliced[k]
            else:
                count += 1
        if count > 1:
            result += (str(count) + before)
        else:
            result += before
        ans=min(ans, len(result))
    return ans

