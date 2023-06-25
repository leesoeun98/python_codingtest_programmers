# 1차 시도 실패 : 10분 소요, 혼자 풂 (시간 초과 - 당연히 최대가 5^20이라서 모두 구해놓고 풀 수 없음)
# 3차 시도 성공 : 1시간 27분 소요, 접근법은 다른사람 풀이 참고 구현은 혼자
# 분할정복 + 누적합으로 4^(n-1) 그룹으로 나눔, 이때 각 그룹의 길이 및 index는 5^(n-1) 몫과 나머지로 구하기
# 0의 위치에 제발 주의해서 예외처리 하기
def solution(n, l, r):
    def calc(value, n):
        sum_v = 0
        while n > 0:
            share = value // (5 ** (n - 1))
            remainder = value % (5 ** (n - 1))

            if 1 <= share <= 2:
                sum_v += share * 4 ** (n - 1)
            elif 3 <= share <= 5:
                sum_v += (share - 1) * 4 ** (n - 1)
            if share == 2:
                break
            value = remainder
            n -= 1
        return sum_v

    return calc(r, n) - calc(l - 1, n)
