"""
1시간 8분, 다른 사람 코드 봄
핵심 포인트
1. 완전 탐색, dfs까지 생각했으나 구현법에서 틀림
2. gap이 최대일때 넣는 것에 주의
3. 정렬 주의
"""
import copy


# dfs 생각까진 함. 구현 못함
def solution(n, info):
    answer, gap = [], 0

    # 점수 차 계산하는 함수
    def calcDiff(info, shots):
        a, l = 0, 0
        for i in range(11):
            if info[i] == shots[i] == 0:
                continue
            if info[i] >= shots[i]:
                a += (10 - i)
            else:
                l += (10 - i)
        return l - a

    def dfs(depth, board, shots):
        nonlocal answer, info, gap
        if depth == 11:
            # shots가 남았으면 10에 몰빵 -> 왜?
            if shots != 0:
                board[10] = shots
            scoreDiff = calcDiff(info, board)
            # 점수차가 0보다 크고 gap보다 크면 넣기
            if scoreDiff > 0 and scoreDiff > gap:
                gap = scoreDiff
                answer = [copy.deepcopy(board)]
            # 점수차가 gap이랑 동일하면 append
            if scoreDiff > 0 and scoreDiff == gap:
                answer.append(copy.deepcopy(board))
            return

        # 점수 먹는 경우 (남은 화살이 info[depth] 보다 많은 경우)
        if info[depth] < shots:
            board.append(info[depth] + 1)
            dfs(depth + 1, board, shots - info[depth] - 1)
            board.pop()

        # 안 먹는 경우
        board.append(0)
        dfs(depth + 1, board, shots)
        board.pop()

    dfs(0, [], n)

    if answer == []:
        return [-1]
    answer.sort(key=lambda x: x[::-1], reverse=True)
    return answer[0]