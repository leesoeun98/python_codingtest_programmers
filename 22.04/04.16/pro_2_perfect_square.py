"""
4분 소요, gcd 구할 때 예전 코드 봄
핵심 포인트
1. 최소 사각형 등장 횟수:gcd(w, h)
2. 최소 사각형 크기: w/gcd(w, h) + h/gcd(w, h) - 1
3. 총 빼야 하는 사각형들: gcd(w, h) * (w/gcd(w, h) + h/gcd(w, h) - 1) == w+h-gcd(w, h)
"""
def solution(W, H):
    def gcd(a, b):
        if b==0:
            return a
        else:
            return gcd(b, a%b)
    return W*H - (W+H-gcd(W, H))
