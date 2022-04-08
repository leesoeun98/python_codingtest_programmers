"""
20분 소요, 예전 코드 봄
핵심 포인트
1. dic에 score들을 저장하겠다
2. for문 밖에서 dic[key].sort()로 한번만 정렬하기
3. 이진탐색으로 score만족 하는 사람 명수 구하되, high랑 temp 주의 (high=l-1, temp=1)
=> while 실행안되면 0명이되야 하니까 1-temp며 temp초기값이 1이어야 함. high는 인덱스 out안되게
"""
def solution(infos, queries):
    dic, res={}, []
    for lang in ["-", "cpp", "java", "python"]:
        for category in ["-","backend","frontend"]:
            for exp in ["-","junior","senior"]:
                for food in ["-", "chicken","pizza"]:
                    dic[lang+category+exp+food]=[]
    for info in infos:
        info_split = info.split(' ')
        for lang in ["-", info_split[0]]:
            for category in ["-", info_split[1]]:
                for exp in ["-", info_split[2]]:
                    for food in ["-", info_split[3]]:
                        dic[lang+category+exp+food].append(int(info_split[4]))
    for key in dic.keys():
        dic[key].sort()
    for query in queries:
        score = int(''.join(query.split(' and ')).split(' ')[1])
        condition = ''.join(query.split(' and ')).split(' ')[0]
        scores = dic[condition]
        l= len(scores)
        low , high, temp= 0, l-1, 0
        #이진 탐색
        while low<=high:
            mid = (low+high)//2
            if scores[mid]<score:
                low = mid+1
            else:
                temp=mid
                high=mid-1
        res.append(l-temp)
    return res
