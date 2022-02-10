def solution(board, moves):
    lst=[]
    count=0
    for move in moves:
        for i in range(len(board[0])):
            if board[i][move-1]!=0:
                if len(lst)>0 and lst[-1]==board[i][move-1]:
                    count+=1
                    lst.pop()
                else:
                    lst.append(board[i][move-1])
                board[i][move-1]=0
                break
    return count*2
"""
문제 진짜 제대로 읽기 => 터진 횟수가 아니라 터진 인형 개수라서 *2만큼 반환임...제발
"""