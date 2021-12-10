class valueofItem:
    def __init__(self, weight, value, factor):
        self.weight = weight
        self.value = value
        self.factor = value / weight

    def __lt__(self, other):
        return self.factor < other.factor  # not sure how it works


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


if __name__ == "__main__":
    value = [5, 10, 20, 50, 100, 200, 450, 1000]  # 5, 2.5, 3.3, 3.125, 4, 6.25
    weight = [1, 4, 6, 16, 24, 32, 36, 40]        # 12.5, 25
    capacity = float(input("Capacity:  "))

    overall = greed.calculateTheValue(weight, value, capacity)
    print("Max value for this capacity is: ", round(overall))
