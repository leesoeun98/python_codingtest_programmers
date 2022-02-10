def solution(absolutes, signs):
    return sum(v if s else -v for v,s in zip(absolutes, signs))