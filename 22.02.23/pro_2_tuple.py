"""
26분 소요
개선 가능한 사항: lstrip, rstrip 후 split 하면 더 간단
"""
def solution(s):
    tuples = s.lstrip('{').rstrip('}').split('},{')
    lst, ans=[], []
    for tuple in tuples:
        lst.append(list(map(int, tuple.split(','))))
    lst.sort(key=lambda x:len(x))
    for line in lst:
        for item in line:
            if item not in ans:
                ans.append(item)
    return ans

"""def solution(s):
    tuples = s[1:-1].split('{')
    lst = []
    for i in range(1, len(tuples)):
        if i != len(tuples) - 1:
            tuple = tuples[i][:-2].strip()
        else:
            tuple = tuples[i][:-1].strip()
        temp = list(map(int, tuple.split(',')))
        lst.append(temp)
    lst.sort(key=lambda x: len(x))
    ans = []
    for order in lst:
        for item in order:
            if item not in ans:
                ans.append(item)
    return ans"""