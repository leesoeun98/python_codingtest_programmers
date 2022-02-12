"""
기본적인 3진법과 동일하나, 3으로 나누어 떨어질때만 다르다. 0이 없기 때문
=> 3으로 나누어 떨어지는 경우 몫을 -1하고 0대신 4를 쓴다.
=> 수가 커질수록 앞에 붙어야하니 숫자를 뒤집어준다.
"""
def solution(n):
    ans=""
    while n!=0:
        remainder=n%3
        n//=3
        if remainder==0:
            n-=1
            ans+="4"
        else:
            ans+=str(remainder)
    return ans[::-1]