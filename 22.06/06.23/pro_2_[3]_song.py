"""
17분 소요, multiple replace는 다른 사람 코드 참조함
핵심 포인트
1. replace로 문자열 간단히
2. length구해서 melody 재구성
3. m이 melody에 있으면 append
4. lst sort
"""
from collections import OrderedDict


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


od = OrderedDict([("C#", 'H'), ('D#', 'I'), ('F#', 'J'), ('G#', 'K'), ('A#', 'L')])


def solution(m, musicinfos):
    m = replace_all(m, od)
    lst = []
    for idx, music in enumerate(musicinfos):
        startTime, endTime, title, melody = music.split(',')
        melody = replace_all(melody, od)
        length = 60 * (int(endTime.split(':')[0]) - int(startTime.split(':')[0])) + (
                    int(endTime.split(':')[1]) - int(startTime.split(':')[1]))

        if len(melody) > length:
            melody = melody[:length]
        else:
            melody = melody * (length // len(melody)) + melody[:(length % len(melody))]

        if m in melody:
            lst.append([idx, length, title])
    lst.sort(key=lambda x: (-int(x[1]), int(x[0])))
    return '(None)' if len(lst) == 0 else lst[0][2]