"""
22분 소요, 스스로 풂
주의할 부분
1. combinations -> 시간 복잡도에서 실패
2. 직접 중복되지 않는것들만 다 취하고 nums에서 해당 item들을 제거한 후, len이 모자라면 마저 채우자
"""


def solution(nums):
    nums = list(map(str, nums))
    phoneketmons, cnt = [], len(nums) // 2
    for phoneketmon in nums:
        if len(phoneketmons) == len(nums) // 2:
            break
        if len(phoneketmons) == 0 or (len(phoneketmons) > 0 and phoneketmon not in phoneketmons):
            phoneketmons.append(str(phoneketmon))
    for phoneketmon in phoneketmons:
        nums.remove(phoneketmon)
    if len(phoneketmons) < cnt:
        phoneketmons += nums[:int(cnt - len(phoneketmons))]
    return len(list(set(phoneketmons)))


