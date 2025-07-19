n, q = map(int, input().split())

nums = list(map(int, input().split()))

for i in range(q):
    com = list(map(int, input().split()))

    if com[0] == 1:
        print(nums[com[1]-1])
    elif com[0] == 2:
        print(nums.index(com[1])+1)
    else:
        for j in range(com[1]-1, com[2]):
            print(nums[j], end=" ")
        print()