"""
30분 소요
도전도 못하고 바로 다른 사람 풀이 봄
핵심 포인트
1. 최소 단위 사각형 찾기, 횟수 찾기
=> 최소 단위 사각형이 반복되는 횟수가 바로 gcd(w, h)
=> 최소 단위 사각형의 가로, 세로는 즉 w/gcd(w, h) 랑 h/gcd(w, h)
=> 최소 단위 사각형에서 대각선이 지나가는 사각형은 w/gcd(w, h)+h/gcd(w, h)-1 (1을 빼는 이유는 맨 처음 가로, 세로에서 한번 겹치므로)
즉, (w/gcd(w, h)+h/gcd(w, h)-1)*gcd(w, h)만큼 제거 해야 하는 것
"""
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

def solution(w, h):
     return w*h-(w+h-gcd(w, h))