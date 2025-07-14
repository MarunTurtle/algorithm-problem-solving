n = int(input())

def total_even(a, b):
    
    total = 0
    for i in range(a, b+1):
        if i % 2 == 0:
            total += i

    return total

for _  in range(n):
    a, b = map(int, input().split()) 
    print(total_even(a, b))
    


