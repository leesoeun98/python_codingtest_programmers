"""
8분 소요, 예전 코드 봄
핵심 포인트
1. gcd(W, H)만큼 최소 단위 사각형이 반복됨
2. 최소 단위 사각형은 좌표가 대각선으로 W/gcd + H/gcd - 1 만큼 이동, 사각형 개수가 곧 이거
3. 즉, 전체 사각형은 W * H - (W/gcd + H/gcd - 1) *gcd = W * H - (W+H-gcd)
"""
def solution(W, H):
    def gcd(a, b):
        if b==0:
            return a
        else:
            return gcd(b, a%b)
    return W * H - (W+H-gcd(W, H))