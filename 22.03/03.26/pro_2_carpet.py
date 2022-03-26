"""
9분 소요, 스스로 풂
완전탐색 답게 모든 경우를 다 탐색하더라도, 가로가 더 길다 했으니 if문으로 시행횟수 줄이기
계산해서 b, y가 brown, yellow와 일치 시 바로 return
"""
def solution(brown, yellow):
    total = brown+yellow
    for i in range(1, total+1):
        if total%i==0 and i>=total//i:
            b = 2*i+2*((total//i)-2)
            y = total-b
            if b==brown and y==yellow:
                return [i, total//i]