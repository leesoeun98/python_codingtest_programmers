def solution(n, lost, reverse):
    #sorting 필수
    lost.sort()
    reverse.sort()
    # 여벌있는 애 중 도둑맞은거부터 제거 + lost에서도 같이 제거 필요
    rev = list(filter(lambda x:x not in lost, reverse))
    lst = list(filter(lambda x:x not in reverse, lost))
    for r in rev:
        if r-1 in lst:
            lst.remove(r-1)
        elif r+1 in lst:
            lst.remove(r+1)
    return n-len(lst)