N = int(input())

# Please write your code here.
def num_sum(x):
    if x == 2:
        return 2
    if x == 1:
        return 1
    
    return x + num_sum(x-2)

print(num_sum(N))