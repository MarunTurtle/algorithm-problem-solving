for i in range(1, 20):
    for j in range(1, 20, 2):
        if j == 19:
            print(f"{i} * {19} = {i*19}")
            continue
        print(' / '.join(f"{i} * {j} = {i*j}" for j in range(j, j+2)))
        