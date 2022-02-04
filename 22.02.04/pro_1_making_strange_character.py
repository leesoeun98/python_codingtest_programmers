"""
하나 이상의 공백이므로, 단어    단어  단어 이런식이면 해당 공백들을 모두 보존해야 함
=> 따라서 strip 쓰면 x split도 split()이면 공백을 모두 없애버리므로 split(" ")로 공백 보존 필요
"""
def solution(s):
    words = s.split(" ")
    final=""
    for word in words:
        for i in range(len(word)):
            if i%2==0:
                final+=word[i].upper()
            else:
                final+=word[i].lower()
        final+=" "
    return final[:-1]