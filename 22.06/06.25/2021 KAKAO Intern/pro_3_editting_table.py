"""
52분 소요, 다른 사람 풀이 봄
핵심 포인트
1. n이 1000000이라서 일반 배열로는 불가, linked list 사용해야 함
=> dict로 구현
=> linked list로 prev, next 정보 이용해서 지우고 커서 이동
"""


def solution(n, k, cmd):
    res, delete = ['O'] * n, []
    table = {i: [i - 1, i + 1] for i in range(n)}
    table[0], table[n - 1] = [None, 1], [n - 2, None]

    for c in cmd:
        if c == 'C':
            res[k] = 'X'
            prev_item, next_item = table[k]
            delete.append([prev_item, next_item, k])
            # k 갱신
            if next_item == None:
                k = table[k][0]
            else:
                k = table[k][1]
            # table 갱신
            if prev_item == None:
                table[next_item][0] = None
            elif next_item == None:
                table[prev_item][1] = None
            else:
                table[prev_item][1] = next_item
                table[next_item][0] = prev_item
        elif c == 'Z':
            prev_item, next_item, now = delete.pop()
            res[now] = 'O'
            # table 갱신
            if prev_item == None:
                table[next_item][0] = now
            elif next_item == None:
                table[prev_item][1] = now
            else:
                table[next_item][0] = now
                table[prev_item][1] = now
        else:
            c1, c2 = c.split(' ')
            c2 = int(c2)
            if c1 == 'D':
                for _ in range(c2):
                    k = table[k][1]
            else:
                for _ in range(c2):
                    k = table[k][0]
    return ''.join(res)


"""
이전코드
def solution(n, k, cmd):
    res=['O']*n
    delete=[]
    for c in cmd:
        if len(c)>1:
            command = c.split(' ')
            if command[0]=='U':
                cnt=res[k-int(command[-1]):k].count('X')
                k-=int(command[-1])
                k-=cnt
            elif command[0]=='D':
                cnt=res[k:k+int(command[-1])].count('X')
                k+=int(command[-1])
                k+=cnt
        elif c=='C':
            res[k]='X'
            delete.append(k)
            if k==n-1:
                k=n-2
            else:
                k+=1
        elif c=='Z':
            res[delete[-1]]='O'
            delete.pop()
    return ''.join(res)
"""
