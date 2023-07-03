# 9분 소요 (혼자 풂) - 출력 빠르게 하기 + 문제 조건 잘 읽기 (알파벳 순 출력)
import sys
n,m = map(int, sys.stdin.readline().split())
name_list={}
for _ in range(n+m):
    name = sys.stdin.readline().strip()
    if name not in name_list:
        name_list[name]=0
    name_list[name]+=1
answer = [name for name, count in name_list.items() if count>1]
answer.sort()
print(len(answer))
for name in answer:
    print(name)