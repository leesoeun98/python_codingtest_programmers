"""
19분 소요, 예전 코드 봄
틀린 부분
1. 이분 탐색!!!!! left, right, temp 변수랑 갱신 조건 헷갈리지 말기
"""
def solution(infos, queries):
    dic, res={}, []
    for lang in ['-', 'cpp', 'java', 'python']:
        for cate in ['-', 'backend', 'frontend']:
            for exp in ['-', 'junior', 'senior']:
                for food in ['-', 'chicken', 'pizza']:
                    dic[lang+cate+exp+food]=[]
    for info in infos:
        items = info.split(' ')
        for lang in ['-', items[0]]:
            for cate in ['-', items[1]]:
                for exp in ['-', items[2]]:
                    for food in ['-', items[3]]:
                        dic[lang+cate+exp+food].append(int(items[4]))
    for key in dic.keys():
        dic[key].sort()
    for query in queries:
        parsed = query.split(' and ')
        condition = parsed[0]+parsed[1]+parsed[2]+parsed[3].split(' ')[0]
        score=int(parsed[3].split(' ')[1])
        #이분 탐색
        left, right = 0, len(dic[condition])-1
        scores, temp = dic[condition], len(dic[condition])
        while left<=right:
            mid = (left+right)//2
            if score<=scores[mid]:
                right = mid - 1
                temp = mid
            else:
                left=mid+1
        res.append(len(dic[condition])-temp)
    return res
