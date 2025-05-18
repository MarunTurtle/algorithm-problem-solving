# def solution(numbers):
#     sum = []
#     length = len(numbers)
#     for i in range(length):
#         for j in range(i + 1, length):
#             sum.append(numbers[i] + numbers[j])
            
#     answer = sorted(set(sum))
    
#     return answer

def solution(numbers):
    return sorted(set(numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))))

"""

def solution(numberes):
    return sorted(set(numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(i+1, len(numbers))))


"""