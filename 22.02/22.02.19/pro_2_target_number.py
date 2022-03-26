count=0
def solution(numbers, target):
    def dfs(depth, cur):
        global count
        if depth == len(numbers):
            if cur == target:
                count += 1
            return count
        else:
            signs=[-cur, +cur]
            if depth==1:
                for i in range(2):
                    dfs(depth+1, signs[i]-numbers[depth])
                    dfs(depth+1, signs[i]+numbers[depth])
            else:
                dfs(depth+1, cur+numbers[depth])
                dfs(depth+1, cur-numbers[depth])
    dfs(1,numbers[0])
    return count