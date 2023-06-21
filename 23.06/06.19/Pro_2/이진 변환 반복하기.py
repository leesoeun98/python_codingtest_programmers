# 9분소요, 혼자 풂 (1차 성공)
# list에서 원소 개수 찾는 count로 풀자
# 0 모두 제거 후, 길이를 2진법으로 표현해서 다시 할당 (1이 될때까지 반복, 이 과정에서 반복 횟수와 제거된 모든 0의 개수를 반환)
def solution(s):
    count, zero = 0, 0
    while s != "1":
        zero += s.count("0")
        new_s = "1" * s.count("1")
        s = bin(len(new_s))[2:]
        count += 1
    return [count, zero]

