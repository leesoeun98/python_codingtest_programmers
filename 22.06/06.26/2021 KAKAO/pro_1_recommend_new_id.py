"""
8분 소요, 스스로 풀었으나 sub 쓰는 법 외부 문서 참고함
핵심 포인트
1. regex
=> ^[] 는 이걸로 시작, []$ 는 이걸로 끝
=> [] {2,} []안의 문자열이 2회이상 반복 시
"""
import re
def solution(new_id):
    new_id=new_id.lower()
    new_id = ''.join(re.findall(r'[a-z0-9-_.]', new_id))
    new_id = re.sub(r'[.]{2,}', '.', new_id)
    new_id = re.sub(r'^[.]|[.]$', '', new_id)
    new_id = 'a' if len(new_id)==0 else new_id[:15]
    new_id = re.sub(r'^[.]|[.]$', '', new_id)
    if len(new_id)<=2:
        new_id += new_id[-1]*(3-len(new_id))
    return new_id