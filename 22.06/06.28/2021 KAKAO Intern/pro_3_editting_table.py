"""
24분 소요, 이전 코드 봄
핵심 포인트
1. 탐색이 너무 오래걸림 -> 이중 연결 리스트 사용
2. 구현력의 문제 table, k, res 갱신에 주의
"""


def solution(n, k, cmd):
    # n, cmd 매우 커서 이중 for문 불가
    # 이중 연결 리스트 쓰자
    res = ['O'] * n
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0], table[n - 1] = [None, 1], [n - 2, None]
    delete = []
    for c in cmd:
        if c[0] == 'D':
            # k 갱신
            for i in range(int(c.split(' ')[1])):
                k = table[k][1]
        elif c[0] == 'U':
            # k 갱신
            for i in range(int(c.split(' ')[1])):
                k = table[k][0]
        elif c[0] == "C":
            # 삭제
            res[k] = 'X'
            prev_item, next_item = table[k]
            if prev_item == None:
                table[next_item][0] = None
            elif next_item == None:
                table[prev_item][1] = None
            else:
                table[prev_item][1] = next_item
                table[next_item][0] = prev_item
            delete.append([prev_item, next_item, k])
            # k 갱신
            if next_item == None:
                k = table[k][0]
            else:
                k = table[k][1]
        else:
            # 복구
            p, n, cur = delete.pop()
            res[cur] = 'O'
            # table 갱신
            if p == None:
                table[n][0] = cur
            elif n == None:
                table[p][1] = cur
            else:
                table[p][1] = cur
                table[n][0] = cur
    return ''.join(res)
