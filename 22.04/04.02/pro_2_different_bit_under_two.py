"""
55분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 짝수면 끝이 0으로 끝나서 +1 하기만 하면 비트 1개 차이나고 항상 큰 최소의 수가 나옴
2. 홀수면 두가지 01 => +1 하면 11로 끝나서 비트 1개 차이나고 항상 큰 최소의 수가 됨
.....11로 끝나면 => 앞 두 자리, 혹은 중간 두 자리만 차이나고 나머진 다 동일하게
이렇게 되려면 2^(마지막 1의 개수 -1)를 더해야 1에서 1을 더해 자릿수 넘어가서 앞만 10으로 바뀌고 뒤는 그대로
"""
"""
시간초과 => 규칙성을 찾아야 함 
def solution(numbers):
    ans=[]
    for number in numbers:
        for i in range(int(number)+1, pow(10,15)):
            if (bin(int(number)^i)).count('1')<=2:
                ans.append(i)
                break
    return ans
"""
def solution(numbers):
    ans=[]
    for number in numbers:
        target = bin(int(number))[2:]
        if target[-2:] in ["01", "10", "00"] or int(number)==1 or int(number)==0:
            ans.append(int(number)+1)
        else:
            for i in range(len(target), 1, -1):
                #끝에서 부터 보기
                if '0' not in target[-i:]:
                    ans.append(number + 2 ** (i - 1))
                    break
    return ans

print(solution([0,779, 343]))
"""
target = bin(int(number))[2:]
            count=0
            for i in range(len(target)-1, -1, -1):
                count+=1
                if target[i]=="0":
                    ans.append(int(number)+2**(count-2))
                    break
"""