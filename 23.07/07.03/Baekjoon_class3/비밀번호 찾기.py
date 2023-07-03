# 10:43
# N이 100만, M도 100만까지 (주소 비밀번호) 탐색 => 해시
import sys
print = sys.stdout.write

n,m = map(int, sys.stdin.readline().split())
address_list={}
for i in range(n):
    address, password = sys.stdin.readline().split()
    address_list[address] = password
for _ in range(m):
    print(address_list[sys.stdin.readline().strip()]+"\n")
