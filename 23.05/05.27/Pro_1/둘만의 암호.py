# 19분 소요, 혼자 풂 (3차 시도에서 성공) / 테스트케이스는 남의 거 참고
# index out of range에 주의하고, 코드 신중히 짜자 +1, %26 같은거 안해서 계속 오류남
alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]


def solution(s, skip, index):
    answer = []
    for letter in s:
        count, targetIndex = 0, alphabetList.index(letter)
        while count != index:
            if alphabetList[(targetIndex + 1) % 26] not in skip:
                count += 1
            targetIndex += 1
        answer.append(alphabetList[targetIndex % 26])
    return ''.join(answer)