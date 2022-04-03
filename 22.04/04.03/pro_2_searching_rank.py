"""
37분 소요, 스스로 풀었으나 효율성에서 0점이라 예전 코드 참고함
핵심 포인트
1. dict를 써야 각 조건별로 모든 사람의 socre을 저장 가능, 속도 빠름
2. score sort는 한번만
3. score을 이분탐색으로 찾기
4. 여기서 틀림 l, temp = len(scores), len(scores) (만약 이분탐색에서 만족 못했으면, l-tmp로 0이 되어야 하므로 temp도 l 값이어야 함)
"""
def solution(infos, queries):
    dic={}
    result=[]
    for lang in ['-', "cpp", "java", "python"]:
        for cate in ["-", "backend", "frontend"]:
            for exp in ["-", "junior", "senior"]:
                for food in ["-", "chicken", "pizza"]:
                    dic[lang+cate+exp+food]=[]
    for idx, info in enumerate(infos):
        infoo = info.split(" ")
        for lang in ["-", infoo[0]]:
            for cate in ["-", infoo[1]]:
                for exp in ["-", infoo[2]]:
                    for food in ["-", infoo[3]]:
                        dic[lang+cate+exp+food].append(int(infoo[4]))
    #점수 여기서 sort해야 시간 효율성 안떨어짐
    for key in dic.keys():
        dic[key].sort()
    for query in queries:
        condition = ''.join(query.split(" and ")).split(" ")[0]
        score = int(''.join(query.split(" and ")).split(" ")[1])
        #이분탐색 써야 효율성 통과 가능
        scores = dic[condition]
        l, temp = len(scores), len(scores)
        low, high = 0, l-1
        while low<=high:
            mid=(low+high)//2
            # scores[mid]가 크거나 같으면 이제 갱신 (temp는 곧 index)
            if score<=scores[mid]:
                temp = mid
                high = mid - 1
            # scores[mid]가 작으면 low를 올려야 함
            else:
                low=mid+1
        result.append(l-temp)
    return result