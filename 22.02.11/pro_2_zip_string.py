"""def solution(s):
    minlen = len(s)
    for unit in range(1, len(s) + 1):
        res = ""
        splitWord = [s[i * unit:unit * (i + 1)] for i in range(len(s) // unit)]
        if len(s[(len(s)//unit)*unit:])>0:
            splitWord.append(s[(len(s)//unit)*unit:])
        i = 0
        if len(splitWord) == 1:
            res += splitWord[-1]
        else:
            while i < len(splitWord):
                count = 1
                while i < len(splitWord)-1 and (splitWord[i] == splitWord[i+1]):
                    count += 1
                    i += 1
                if count != 1:
                    res += str(count)
                res += splitWord[i]
                i += 1
        if minlen > len(res):
            minlen = len(res)
    return minlen"""

def solution(s):
    minlen = len(s)
    for unit in range(1, len(s) + 1):
        res = ""
        splitWord = [s[i * unit:unit * (i + 1)] for i in range(len(s) // unit)]
        if len(s[(len(s)//unit)*unit:])>0:
            splitWord.append(s[(len(s)//unit)*unit:])
        cur_cnt, cur_word=0, splitWord[0]
        for a, b in zip(splitWord, splitWord[1:]+['']):
            if a==b:
                cur_cnt+=1
            else:
                if cur_cnt>1:
                    res+=cur_cnt
                res+=cur_word
                cur_word=b
                cur_cnt=1
        print(res)
        if minlen > len(res):
            minlen = len(res)
    return minlen