"""
5분 소요, 스스로 풂
핵심 포인트
1. string을 파싱해서 순서대로 sort하는 배열 만들기
2. 각 배열의 원소들 중에서 ans에 없으면 append
=> 결국 문제 이해가 핵심
"""
def solution(s):
    s, candidate, ans = s[2:-2], [], []
    tuples = s.split('},{')

    for tuple in tuples:
        candidate.append(tuple.split(','))
    candidate.sort(key=lambda x: len(x))

    for can in candidate:
        for item in can:
            if int(item) not in ans:
                ans.append(int(item))
    return ans