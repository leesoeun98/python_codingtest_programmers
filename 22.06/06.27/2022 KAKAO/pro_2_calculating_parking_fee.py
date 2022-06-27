"""
19분 소요, 스스로 풂
핵심 포인트
1. dict 잘 이용해서 말그대로 구현하기
2. time 총합에서 fee 계산하는 것에 주의
3. dict sort 주의
"""
import math


def solution(fees, records):
    cars, res = {}, {}
    for record in records:
        time, car, state = record.split(' ')
        if car not in cars:
            cars[car] = []
        cars[car].append([time, state])

    for car, recs in cars.items():
        fee, time = 0, 0
        if len(recs) % 2 == 1:
            recs.append(["23:59", "OUT"])
        for i in range(0, len(recs) - 1, 2):
            time += (int(recs[i + 1][0].split(":")[0]) - int(recs[i][0].split(":")[0])) * 60 + int(
                recs[i + 1][0].split(":")[1]) - int(recs[i][0].split(":")[1])
        if time <= fees[0]:
            fee += fees[1]
        else:
            fee += fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
        res[int(car)] = fee
    res = dict(sorted(res.items(), key=lambda x: x[0]))
    return [value for key, value in res.items()]