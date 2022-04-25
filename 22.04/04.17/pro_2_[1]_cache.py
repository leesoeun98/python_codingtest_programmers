"""
27분 소요, 스스로 풂 (그러나 테케, 힌트 봄)
핵심 포인트
1. 순서대로 구현하면 됨 (cache hit, cache miss)
2. LRU 주의
=> min 값을 찾아서 pop, 혹은 min이 여러개면 가장 마지막에 사용된 맨 앞꺼 pop
=> cache hit였으면 target을 가장 끝에 append
=> cache miss 였으면 target count+=1 하고 가장 끝에 append
"""
def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities)*5

    cache, time = [["",0]]*cacheSize, 0
    for city in cities:
        cache_cities, city_any = [item[0] for item in cache], city.lower()
        #cache miss -> cache가 비어져 있으면 아무거나 pop, 아니면 제일 count가 min값이면서 가장 먼저 있는애 pop -> append([city_any, 0])
        if city_any not in cache_cities:
            time+=5
            if cache.count(["", 0])>0:
                target = cache.index(["", 0])
                cache.pop(target)
            else:
                least = list(filter(lambda x: (x[1]==min([count for name, count in cache]) or (cache.index(x)==0)), cache))[0]
                idx = cache.index(least)
                cache.pop(idx)
            cache.append([city_any, 1])
        #cache hit -> count증가
        else:
            time+=1
            target = list(filter(lambda x: x[0] == city_any, cache))[0]
            target_idx = cache.index(target)
            cache.pop(target_idx)
            cache.append([city_any, target[1]+1])
    return time