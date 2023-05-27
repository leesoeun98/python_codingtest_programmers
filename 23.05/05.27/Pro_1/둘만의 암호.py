# 19분 소요, 혼자 풂 (3차 시도에서 성공) / 테스트케이스는 남의 거 참고
# index out of range에 주의하고, 코드 신중히 짜자 +1, %26 같은거 안해서 계속 오류남
# 어차피 skip에 있는 문자열은 계속 포함이 안되니까 빼고 시작하자


def solution(s, skip, index):
    alphabetList = [chr(a) for a in range(ord('a'), ord('z')+1) if chr(a) not in skip]
    answer = []
    for letter in s:
        answer.append(alphabetList[(alphabetList.index(letter)+index) % len(alphabetList)])
    return ''.join(answer)