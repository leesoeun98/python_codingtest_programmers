"""아래 코드는 정답 모두 통과, 효율성 0점 (스스로 풀었고, 1시간 가량 걸림)"""
"""def solution(info, query):
    people=[[] for _ in range(5)]
    for person in info:
        infos = person.split(" ")
        for i in range(5):
            people[i].append(infos[i])
    ans=[]
    for q in query:
        q = q.replace("and", " ")
        qs = q.split(" ")
        final_query = [x for x in qs if x]
        temp=[i for i in range(len(info))]
        for i in range(5):
            if final_query[i]=='-':
                continue
            else:
                if i==4:
                    for j in temp[:]:
                        if int(people[i][j]) < int(final_query[i]):
                            temp.remove(j)
                else:
                    for j in temp[:]:
                        if people[i][j] != final_query[i]:
                            temp.remove(j)
        ans.append(len(temp))
    return ans
"""
"""
dict 이용하기
"""
"""아래 코드는 정답 모두 통과, 효율성 0점 (스스로 풀었고, 1시간 가량 걸림)"""
"""def solution(info, query):
    people=[[] for _ in range(5)]
    for person in info:
        infos = person.split(" ")
        for i in range(5):
            people[i].append(infos[i])
    ans=[]
    for q in query:
        q = q.replace("and", " ")
        qs = q.split(" ")
        final_query = [x for x in qs if x]
        temp=[i for i in range(len(info))]
        for i in range(5):
            if final_query[i]=='-':
                continue
            else:
                if i==4:
                    for j in temp[:]:
                        if int(people[i][j]) < int(final_query[i]):
                            temp.remove(j)
                else:
                    for j in temp[:]:
                        if people[i][j] != final_query[i]:
                            temp.remove(j)
        ans.append(len(temp))
    return ans
"""
"""
<효율성 높이기>
1. dict 이용하기 (hash)
2. sort는 무조건 for문 밖에서
3. 탐색이 오래걸린다면 무조건 이분탐색 쓰기 
"""


def solution(info, queries):
    answer = []
    info_dict = {}
    for lang in ["cpp", "java", "python", "-"]:
        for job in ["backend", "frontend", "-"]:
            for exp in ["junior", "senior", "-"]:
                for food in ["chicken", "pizza", "-"]:
                    info_dict[lang + job + exp + food] = []

    for person in info:
        infos = person.split(" ")
        for lang in [infos[0], "-"]:
            for job in [infos[1], "-"]:
                for exp in [infos[2], "-"]:
                    for food in [infos[3], "-"]:
                        info_dict[lang + job + exp + food].append(int(infos[4]))
    # 각 조건별 사람들의 코테 점수 sort
    for key in info_dict.keys():
        info_dict[key].sort()

    for query in queries:
        query = query.replace(" and ", " ")
        query = query.split(" ")
        key = ''.join(query[:-1])
        query_score=int(query[-1])
        #이분탐색 안쓰면 효율성 0
        info_score=info_dict[key]
        l= len(info_score)
        tmp=l
        low, high = 0, l-1
        while low<=high:
            mid=(low+high)//2
            # info_score[mid]가 기준점수보다 크면 tmp에 mid값 넣고, high를 이동
            if query_score<=info_score[mid]:
                tmp=mid
                high=mid-1
            else:
                low=mid+1
            # 기준점수가 더 크면 low를 이동
        answer.append(l-tmp) # l명중 index가 tmp 이상인 애들 == l - tmp
    return answer

