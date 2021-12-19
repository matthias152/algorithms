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
