def solution(N, A, B):
    round = 1

    def NextRound(num):
        if num % 2 == 0:
            num //= 2
        else:
            num //= 2
            num += 1
        return num

    while True:
        if B-A==1 and B % 2 == 0 and A % 2 == 1:
            return round
        elif A-B == 1 and A % 2 == 0 and B % 2 == 1:
            return round
        A, B = NextRound(A), NextRound(B)
        round += 1
