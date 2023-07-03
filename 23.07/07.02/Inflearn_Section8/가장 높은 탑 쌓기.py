# 넓이, 무게로 오름차순 정렬 후 => dp는 높이에 대한 배열
dp=[]

def problem():
    dp=[0]*len(lst)
    for i in range(len(lst)):
        height = 0
        for j in range(i-1, 0, -1):
            if lst[j][0]<lst[i][0] and lst[j][2]<lst[i][2] and height<dp[j]:
                height = dp[j]
        dp[i]=height+lst[i][1]
    print(dp)
    return max(dp)

n = int(input())
lst=[]
for _ in range(n):
    a, b, c = map(int, input().split(' '))
    lst.append([a, b, c])
lst.sort(key=lambda x:(x[0], x[1]))
print(problem())
