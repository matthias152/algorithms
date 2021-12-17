from dynamicc import dynamic
from brute import brute
from greedy import *


value = [5, 10, 20, 50, 100, 200, 450, 1000]
weight = [1, 4, 6, 16, 24, 32, 36, 40]
q = len(value)


while True:
    capacity = int(input("Capacity: "))
    c = int(input("Which method you want to use? (1-B, 2-G, 3-D, 4 for quit): "))

    match c:
        case 1:
            print("Max value for this capacity is: ", brute(capacity, weight, value, q))

        case 2:
            print("Max value for this capacity is: ", round(greed.calculateTheValue(weight, value, capacity)))

        case 3:
            print("Max value for this capacity is:", dynamic(capacity, weight, value))

        case 4:
            print("Quitted.")
            quit()
        case _:
            print("Wrong answer")
            quit()
