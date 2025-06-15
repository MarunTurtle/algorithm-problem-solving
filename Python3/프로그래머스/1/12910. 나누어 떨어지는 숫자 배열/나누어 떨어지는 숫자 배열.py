def solution(arr, divisor):
    
    answer = [num for num in arr if num % divisor == 0]
    
    return [-1] if len(answer) == 0 else sorted(answer)