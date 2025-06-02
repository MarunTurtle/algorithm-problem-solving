# def solution(arr, divisor):
    
#     answer = []    
    
#     for num in arr:
#         if num % divisor == 0:
#             answer.append(num)
    
#     if len(answer) == 0 : answer = [-1]
    
#     return sorted(answer)

def solution(arr, divisor):
    answer = [num for num in arr if num % divisor == 0]
    return sorted(answer) if answer else [-1]