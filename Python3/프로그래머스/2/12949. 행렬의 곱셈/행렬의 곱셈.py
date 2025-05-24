def solution(arr1, arr2):
    
    row_count = len(arr1)
    col_count = len(arr2[0])
    common_dim = len(arr2)
        
    answer = [[0 for _ in range(col_count)] for _ in range(row_count)]
    
    for i in range(row_count):
        for j in range(col_count):
            for k in range(common_dim):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer