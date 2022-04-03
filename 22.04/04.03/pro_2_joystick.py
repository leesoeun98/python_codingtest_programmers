"""
48분소요, 다른 사람 풀이 봄
핵심 포인트
1. 문자열 모든 경우의 수 다 구하기...여기서 헤맴
2. 왼오 이동 구하기 count=i+len(value)-1 (단, 마지막은 이동 불필요라 -1)
3. 위아래 이동 구하기
4. 처음부터 A로만 된 경우 제거하기 아오 이때 결과는 {"A"}임
"""
def solution(name):
    if set(name)=={"A"}:
        return 0
    ans=int(1e9)
    #조이스틱은 어차피 한 방향으로 이동하면서 바꾸는게 최소가 아닐수도, 오른쪽에서 왼쪽으로 혹은 왼에서 오른쪽으로 이동할 수도 있음
    #조이스틱은 첫 번째 위치부터 시작이라 가정
    for i in range(len(name) // 2):  # 반 이상 움직일 필요 없음
        left_moved = name[-i:] + name[:-i]
        right_moved = name[i:] + name[:i]
        for value in [left_moved, right_moved[0] + right_moved[:0:-1]]:
            #A제거
            while value and value[-1]=='A':
                value=value[:-1]
            # 마지막엔 커서 오른쪽으로 안움직여도 됨
            count=i+len(value)-1
            for alphabet in value:
                count+= min(ord(alphabet)-ord('A'), 26-(ord(alphabet)-ord('A')))
            ans = min(count, ans)
    return ans

