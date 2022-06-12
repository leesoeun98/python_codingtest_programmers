"""
25분 소요, 예전 코드 봄
틀린 부분
1. regex pattern 다 까먹음 ㅠㅠ
"""
import re
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    new_id = re.sub(r'\.+','.',new_id)
    new_id = re.sub('^[.]|[.]$','',new_id)
    new_id = 'a' if new_id=="" else new_id[:15]
    new_id = re.sub('[.]$','',new_id)
    if len(new_id)<3:
        new_id += new_id[-1]*(3-len(new_id))
    return new_id



"""
def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
"""