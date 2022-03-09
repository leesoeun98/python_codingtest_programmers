"""
백준 리모컨과 유사한 문제,
남의 풀이 봄.. 1시간 30분 정도 걸림
"""
def solution(name):
    if set(name) =={'A'}: #모두 A인 경우도 고려 필요
        return 0
    answer=float('inf')
    for i in range(len(name)//2): # 절반만 확인 하면 됨
        left_moved = name[-i:] + name[:-i]
        right_moved = name[i:] + name[:i]
        print(left_moved, right_moved)
        for n in [left_moved, right_moved[0] + right_moved[:0:-1]]: # 왼->오, 오->왼 이동 가능한 모든 문자열, (left_moved, right_moved 뒤에서 앞으로 거꾸로 간 문자열 2가지 경우)
            while n and n[-1]=='A':
                n=n[:-1] # A 모두 제거
            row_move = i+len(n)-1 # 조이스틱이 양옆으로 이동한 count
            col_move = 0 # 조이스틱이 위아래로 이동한 count
            for col in n:
                col_move+=min(ord(col)-ord('A'), 26-(ord(col)-ord('A')))
            answer=min(answer, col_move+row_move)
    return answer
