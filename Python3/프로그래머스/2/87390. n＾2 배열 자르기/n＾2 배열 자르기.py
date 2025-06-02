def solution(n, left, right):
    answer = []
    
    for i in range(left, right + 1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)
        
    return answer



# def solution(n, left, right):
    
#     answer = [[0] * n for _ in range(n)]
#     sol = []
        
#     for i in range(n):
#         for j in range(n):
#             answer[i][j] = max(i, j) + 1
#             sol.append(answer[i][j])
    
#     return sol[left : right+1]