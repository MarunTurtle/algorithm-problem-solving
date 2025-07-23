N = int(input())

# Please write your code here.
def get_sum(x):
    if x == 1:
        return 1
    return get_sum(x-1) + x

print(get_sum(N))