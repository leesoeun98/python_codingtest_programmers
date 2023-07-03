# 4분 소요, 혼자 풂 => 그리디
# 가장 큰값부터 순서대로 하되, 만약 아예 나눠지지 않으면 어차피 몫이 0이고 나머지는 그대로인데 다음 동전으로 넘어감
import sys

n, k = map(int, sys.stdin.readline().split())
coin, answer = [], 0
for _ in range(n):
    coin.append(int(sys.stdin.readline().strip()))
coin.sort(reverse=True)

for c in coin:
    answer += (k // c)
    k = (k % c)

print(answer)
