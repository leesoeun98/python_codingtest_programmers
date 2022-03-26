"""
3마리 뽑아야 하는데 포켓몬 [3,3,3,1,2,4]=>[3,1,2,4]면 len(nums)//2가 답
3마리 뽑아야 하는데 포케몬 [3,3,3,3,3,1]=>[3,1]이면 len(set(nums))가 답
"""
def solution(nums):
    l1, l2 = len(nums)//2, len(set(nums))
    return l2 if l1>l2 else l1
