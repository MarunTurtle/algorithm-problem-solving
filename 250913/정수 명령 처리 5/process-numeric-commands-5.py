N = int(input())

num = []

for _ in range(N):
    line = input().split()
    command = line[0]
    if command == "push_back":
        x = int(line[1])
        num.append(x)
    elif command == "pop_back":
        num.pop()
    elif command == "size":
        print(len(num))
    elif command == "get":
        k = int(line[1])
        print(num[k-1])


# Please write your code here.
