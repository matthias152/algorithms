def dynamic(capacity, weight, value):
    q = len(value)
    t = [[0 for x in range(capacity + 1)] for x in range(q + 1)]

    for i in range(q + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                t[i][j] = 0
            elif weight[i-1] <= j:
                t[i][j] = max(value[i-1] + t[i-1][j-weight[i-1]],  t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[q][capacity]


value = [5, 10, 20, 50, 100, 200, 450, 1000]
weight = [1, 4, 6, 16, 24, 32, 36, 40]
capacity = int(input("Capacity:  "))

print("Max value for this capacity is:", dynamic(capacity, weight, value))
