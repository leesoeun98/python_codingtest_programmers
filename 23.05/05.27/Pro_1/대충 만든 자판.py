# 17:55 - 18:05
# 1,2,3.. 키 숫자마다 매핑된 문자 / 입력하려는 문자열배열 => 각 문자열 작성 시 키 최소로 몇 번 누르면 가능한지

# 각 문자마다 몇번 눌러야 최소로 가능한지 dict 구성 (한 문자마다 여러 키에서 입력 가능하면 최소인 걸로 유지)
keyCountDict = dict()


def solution(keymap, targets):
    for key in keymap:
        for i in range(len(key)):
            if key[i] in keyCountDict.keys():
                keyCountDict[key[i]] = min(i + 1, keyCountDict[key[i]])
            else:
                keyCountDict[key[i]] = i + 1

    answer = []
    for target in targets:
        count = 0
        flag = True
        for letter in target:
            if letter in keyCountDict.keys():
                count += keyCountDict[letter]
            else:
                flag = False
                break
        answer.append(-1 if not flag else count)

    return answer