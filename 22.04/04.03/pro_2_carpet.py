"""
4분 소요, 스스로 풂
핵심 포인트
1. 가로가 더 길거나 같을 수 있음에 주의, 후보군 만들기
2. 후보군 내에서 brown 개수로 탐색, 찾으면 바로 return
"""
def solution(brown, yellow):
    total = brown+yellow
    candidate=[]
    for i in range(2, total+1):
        if total%i==0 and total//i >= i:
            candidate.append([total//i, i])
    for c in candidate:
        if c[1]*2+(c[0]-2)*2==brown:
            return c