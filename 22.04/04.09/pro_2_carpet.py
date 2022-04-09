"""
4분 소요, 스스로 풂
핵심 포인트
1. candidate만들때 가로가 더 길거나 같음에 주의
2. brown개수 조건 충족 시 바로 return
"""
def solution(brown, yellow):
    total = brown+yellow
    candidate=[]
    for i in range(1, total+1):
        if total%i==0 and i>=total//i:
            candidate.append([i, total//i])
    for candi in candidate:
        if brown==candi[0]*2+(candi[1]-2)*2:
            return candi
