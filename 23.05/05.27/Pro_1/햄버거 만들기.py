# 24:18 -
# 1231 이 stack에 순서대로 쌓여있을때만 햄버거 만듦 => list가 주어질때 만들 수 있는 햄버거 개수 int return
# 1차 시도 : 13분 소요, 혼자 풂 (정답인 것 같으나 시간 초과)
def solution(ingredient):
    answer, ingredient_s = 0, ''.join(map(str, ingredient))
    while True:
        idx = ingredient_s.find("1231")
        if idx == - 1:
            break
        else:
            answer += 1
            ingredient_s = ingredient_s[:idx] + ingredient_s[idx+4:]
    return answer