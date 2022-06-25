"""
44분 소요, 다른 사람 풀이 봄
핵심 포인트
1. 효율성 때문에 이중 for문 절대 불가, 투 포인터 문제
2. 투포인터 말그대로 구현하기
=> 보석 채워넣기
=> 보석이 다 있으면 start를 줄여가며 갱신
"""
def solution(gems):
    ans, target_length, start, end = [0,len(gems)], len(set(gems)), 0, 0
    gem_dict={gems[0]:1} # 보석 종류별 개수

    while end<len(gems) and start<len(gems):
        # 모든 보석이 있을 때
        if len(gem_dict)==target_length:
            # 구간 길이가 더 짧으면 ans 갱신
            if end-start < ans[1]-ans[0]:
                ans = [start+1, end+1]
            # 구간 길이 줄이기 위해 start 이동
            else:
                gem_dict[gems[start]] -= 1
                if gem_dict[gems[start]]==0:
                    del gem_dict[gems[start]]
                start += 1
        # 보석 없으니까 end 이동
        else:
            end+=1
            if end==len(gems):
                break
            # gem_dict에 보석 추가
            if gems[end] not in gem_dict:
                gem_dict[gems[end]]=0
            gem_dict[gems[end]]+=1
    return ans