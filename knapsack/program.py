class valueofItem:
    def __init__(self, weight, value, factor):
        self.weight = weight
        self.value = value
        self.factor = value / weight

    def __lt__(self, other):
        return self.factor < other.factor


class greed:
    @staticmethod
    def calculateTheValue(weight, value, capacity):
        items = []
        for i in range(len(weight)):
            items.append(valueofItem(weight[i], value[i], i))
        items.sort(reverse=True)
        total = 0

        for j in items:
            curweight = float(j.weight)
            curvalue = float(j.value)
            if capacity - curweight >= 0:
                capacity -= curweight
                total += curvalue

        return total


def dynamic(capacity, weight, value):
    q = len(value)
    table = [[0 for x in range(capacity + 1)] for x in range(q + 1)]

    for i in range(q + 1):
        for j in range(capacity + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif weight[i-1] <= j:
                table[i][j] = max(value[i-1] + table[i-1]
                                  [j-weight[i-1]],  table[i-1][j])
            else:
                table[i][j] = table[i-1][j]
    return table[q][capacity]


def brute(capacity, weight, value, quantity):
    if q == 0 or capacity == 0:
       return 0
    if (weight[q - 1] > capacity):
       return brute(capacity, weight, value, q - 1)
    else:
       return max(value[q - 1] + brute(capacity - weight[q - 1], weight, value, q - 1),
                  brute(capacity, weight, value, q-1))


value = [5, 10, 20, 50, 100, 200, 450, 1000]
weight = [1, 4, 6, 16, 24, 32, 36, 40]
q = len(value)
capacity = int(input("Capacity:  "))
overall = greed.calculateTheValue(weight, value, capacity)

c = int(input("Which method you want to use? (1-B, 2-G, 3-D)"))

if c == 1:
    print("Max value for this capacity is: ",
          brute(capacity, weight, value, q))
elif c == 2:
    print("Max value for this capacity is: ", round(overall))
elif c == 3:
    print("Max value for this capacity is:", dynamic(capacity, weight, value))
else:
    print("Wrong")
