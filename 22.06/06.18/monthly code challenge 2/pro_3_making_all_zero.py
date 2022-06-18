"""
34분 소요, 다른 사람 코드 봄
1. 일단 tree라면 dfs
=> 인접 리스트 구성하기 tree면
2. 모든 node의 합이 0이면 가능, 아니면 불가능
3. 0번째를 root node로 삼고 dfs 진행
=> dfs는 인접 node들에 대해 탐색, 해당 node 미방문 시, 방문한걸로 하고 다시 dfs에 인접 node 넣기
=> a[start], answer 갱신
"""
import sys

sys.setrecursionlimit(300000)


def solution(a, edges):
    tree = [[] for i in range(len(a))]
    visited = [0] * len(a)
    answer = 0
    for edge in edges:
        tree[edge[0]].append(edge[1])
        tree[edge[1]].append(edge[0])

    def dfs(start, a):
        nonlocal tree, edges, answer
        visited[start] = 1
        for node in tree[start]:
            if visited[node] == 0:
                a[start] += dfs(node, a)
        answer += abs(a[start])
        return a[start]

    if sum(a) == 0:
        dfs(0, a)
        return answer
    else:
        return -1
