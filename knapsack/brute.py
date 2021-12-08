# brute force 

def backpack(capacity, weight, value, quantity):
    if quantity == 0 or capacity == 0:
       return 0
    if (weight[quantity - 1] > capacity):
       return backpack(capacity, weight, value, quantity - 1)
    else:
       return max(value[quantity-1] + backpack(capacity-weight[quantity-1], weight, value, quantity-1),
       backpack(capacity, weight, value, quantity-1))

value = [5, 10, 20, 50, 100, 200, 450, 1000]
weight = [1, 4, 8, 16, 24, 32, 36, 40]
quantity = len(value)
capacity = int(input ("Capacity:  "))

print("Max value for this capacity is: ")
print(backpack(capacity, weight, value, quantity))
