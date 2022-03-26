def solution(numbers, hand):
    dic={1:'L',4:'L',7:'L',3:'R',6:'R',9:'R'}
    ans=""
    left, right=-2,-1
    keypad=[[1,2,3],[4,5,6],[7,8,9],[-2,0,-1]]

    for num in numbers:
        if num in dic:
            ans+=dic[num]
            if dic[num]=="L":
                left=num
            else:
                right=num
        else:
            idx1,idx2=[(i,j) for i in range(4) for j in range(3) if keypad[i][j]==num][0]
            lidx1, lidx2 = [(i, j) for i in range(4) for j in range(3) if keypad[i][j] == left][0]
            ridx1, ridx2 = [(i, j) for i in range(4) for j in range(3) if keypad[i][j] == right][0]
            if abs(idx1-lidx1)+abs(idx2-lidx2)>abs(idx1-ridx1)+abs(idx2-ridx2):
                ans+="R"
                right=num
            elif abs(idx1-lidx1)+abs(idx2-lidx2)<abs(idx1-ridx1)+abs(idx2-ridx2):
                ans+="L"
                left=num
            else:
                if hand=="left":
                    left=num
                    ans+="L"
                else:
                    right=num
                    ans+="R"
    return ans