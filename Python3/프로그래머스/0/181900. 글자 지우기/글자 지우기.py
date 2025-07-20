def solution(my_string, indices):
    new_string = list(my_string)
    
    for idx in indices:
        new_string[idx] = ""
        
    return ''.join(new_string)