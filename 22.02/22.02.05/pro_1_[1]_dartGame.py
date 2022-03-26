"""
regex와 딕셔너리 사용하기
dart[i-1]*=2 하는 부분에선 이미 dart[i]를 시행 시 dart[i-1]은 숫자이므로 단순히 2만 곱해주면 됨
"""
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
    print(dart)
    answer = sum(dart)
    return answer


"""
import math
times=["","",""]
def solution(dartResult):
    ans=[]
    dartResult=dartResult.replace('10','k')
    if dartResult[2].isdigit() or dartResult[2]=='k':
        times[0]=dartResult[:2]
        if dartResult[4].isdigit() or dartResult[4]=='k':
            times[1] = dartResult[2:4]
            times[2] = dartResult[4:]
        else:
            times[1] = dartResult[2:5]
            times[2]=dartResult[5:]
    else:
        times[0]=dartResult[:3]
        if dartResult[5].isdigit() or dartResult[5]=='k':
            times[1] = dartResult[3:5]
            times[2] = dartResult[5:]
        else:
            times[1] = dartResult[3:6]
            times[2] = dartResult[6:]
    for i in range(3):
        temp=0
        if times[i][0]=='k':
            target=10
        else:
            target=int(times[i][0])
        if times[i][1]=='S':
            temp+=target
        elif times[i][1]=='D':
            temp+=math.pow(target,2)
        else:
            temp+=math.pow(target,3)
        if '#' in times[i]:
            temp*=-1
        elif '*' in times[i]:
            temp*=2
            if len(ans)!=0:
                ans[-1]*=2
        ans.append(temp)
    return sum(ans)

"""
