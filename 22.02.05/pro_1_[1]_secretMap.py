def solution(n, arr1, arr2):
    map = []
    for first, second in zip(arr1, arr2):
        temp = str(bin(first | second)[2:])
        temp = temp.rjust(n, '0')
        temp = temp.replace('0', ' ')
        temp = temp.replace('1', '#')
        map.append(temp)
        print(temp)


"""
def solution(n, arr1, arr2):
    map = []
    for i in range(n):
        first = bin(arr1[i])
        second = bin(arr2[i])
        temp = []
        nfirst = first[:2] + '0' * (n + 2 - len(first)) + first[2:]
        nsecond = second[:2] + '0' * (n + 2 - len(second)) + second[2:]

        for i in range(n):
            if int(nfirst[i + 2]) | int(nsecond[i + 2]) == 1:
                temp.append('#')
            else:
                temp.append(' ')
        map.append(''.join(temp))
    return map
"""