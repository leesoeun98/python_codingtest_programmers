"""
27분 소요, 스스로 풂
핵심 포인트
1. dict로 정해진 key, value 미리 다 저장
2. dict 한번만 정렬
3. 이분탐색으로 명수 찾기 (효율성) 단, 이때 right는 len(candidate)-1 이어야 index error 안남
"""
def solution(infos, queries):
    # 4개 항목 key, 코테 점수 value
    dic, res={}, []
    for lang in ['cpp', 'java', 'python', '-']:
        for section in ['backend', 'frontend', '-']:
            for exp in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    dic[lang+section+exp+food]=[]
    for info in infos:
        info = info.split(' ')
        for lang in [info[0], '-']:
            for section in [info[1], '-']:
                for exp in [info[2], '-']:
                    for food in [info[3], '-']:
                        dic[lang+section+exp+food].append(int(info[4]))
    # value들 오름차순 sort
    for key, value in dic.items():
        value.sort()
    # 후보군 찾고, 그 안에서 코테 점수 만족하는 명수 세기
    for query in queries:
        info = query.split(' and ')
        candidate= dic[info[0]+info[1]+info[2]+info[3].split(' ')[0]]
        target_score = int(info[3].split(' ')[1])
        # 이분 탐색으로 명수 탐색
        left, right = 0, len(candidate)-1
        while left<=right:
            # mid가 idx => candidate[mid]==score
            mid = (left+right)//2
            # mid를 작은쪽으로 이동
            if candidate[mid] >= target_score:
                right = mid-1
            else:
                left = mid+1
        res.append(len(candidate)-left)
    return res