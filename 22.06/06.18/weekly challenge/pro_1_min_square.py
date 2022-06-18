"""
3분 소요, 스스로 풂
"""
def solution(sizes):
    # 가로는 항상 큰 거, 세로는 항상 작은거 (방향 정해주기)
    # 모든 명함 다 들어가야 해서 한 방향으로 정렬 시 가장 큰 면적이 답
    return max([max(x, y) for x, y in sizes])*max([min(x, y) for x, y in sizes])