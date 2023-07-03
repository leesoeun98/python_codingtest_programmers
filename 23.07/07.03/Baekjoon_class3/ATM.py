# 6분 소요, 혼자 풂 (그리디 + 정렬)
# N이 1000까지 일 때, 기다리는 시간을 최소로 하려면 그냥 시간을 오름차순 sort한 게 최소 임
# (어차피 어떻게 세우든 뽑는 시간은 동일하고 기다리는 시간을 최소로 해야 하므로)
# 총 소요 시간은 각 원소마다 len()-i를 곱하면 됨
import sys
n = int(sys.stdin.readline().strip())
people = list(map(int, sys.stdin.readline().split()))
people.sort()

time = 0
for i in range(n):
    time += people[i]*(n-i)
print(time)
