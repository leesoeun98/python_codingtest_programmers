"""
30분 소요, 다른 사람 코드 봄
핵심 포인트
1. dfs로 푸는거까진 맞음, 인접 리스트 구성도 함
=> 근데 dfs 구현을 완벽히 못함..
어차피 한번 visit한 곳은 상관 없어서 set에 next들 넣기
"""


def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    res = 1
    for edge in edges:
        # 단방향으로
        tree[edge[0]].append(edge[1])

    def dfs(w, s, node, possible_next):
        nonlocal tree, res
        # set인 가능 경로 매번 update
        res = max(res, s)
        possible_next.update(tree[node])
        for next in possible_next:
            # 늑대면
            if info[next]:
                if s != w + 1:
                    dfs(w + 1, s, next, possible_next - {next})
            else:
                dfs(w, s + 1, next, possible_next - {next})

    dfs(0, 1, 0, set())
    return res