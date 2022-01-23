def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        temp=[]
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    return answer

def sumMatrix(A, B):
    return [[c+d for c, d in zip(a, b)] for a, b in zip(A, B)]

print(sumMatrix([[1,2],[2,3]], [[3,4],[5,6]]))