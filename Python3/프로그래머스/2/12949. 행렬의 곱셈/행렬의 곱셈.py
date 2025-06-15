def solution(arr1, arr2):
    row_cnt = len(arr1)
    col_cnt = len(arr2[0])
    denom_cnt = len(arr2)
    
    answer = [[0] * col_cnt for _ in range(row_cnt)]
    
    for i in range(row_cnt):
        for j in range(col_cnt):
            for k in range(denom_cnt):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer