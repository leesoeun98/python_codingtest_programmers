"""
17분 소요, 예전 코드 봄 (양옆 이동에서)
핵심 포인트
1. i만큼 시작점 미리 이동해서 왼, 오 한 방향으로 가는 문자열 모두 만들기
2. A제거하기
3. 모두 A면 0 return
"""
def solution(name):
    if set(name) == {"A"}:
        return 0
    ans = int(1e9)
    for i in range(len(name)//2):
        # 왼쪽 방향으로만 이동하는 경우, 오른쪽으로만 이동하는 경우 모두 고려, 단 시작점은 꼭 0번째가 아닐 수 있음 (i만큼 미리 이동한 것)
        left, right = name[-i:] + name[:-i], name[i:] + name[:i]
        # 거꾸로 가되 첫 글자는 제외
        for value in [left, right[0] + right[:0:-1]]:
            while value and value[-1] == 'A':
                value = value[:-1]
            # 좌우 이동
            count = i + len(value) - 1
            for v in value:
                count += min(ord(v) - ord('A'), 26 - (ord(v) - ord('A')))
            ans = min(ans, count)
    return ans


