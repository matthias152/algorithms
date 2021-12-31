from dynamicc import dynamic
from brute import brute
from greedy import *
from timeit import default_timer as timer
import random


value = [5, 10, 20, 50, 100, 200, 450, 1000]
weight = [1, 4, 6, 16, 24, 32, 36, 40]
file1 = open("numbers.txt", "a")
file2 = open("values.txt", "r")

r = int(input("RNG - 1, READ - 2, CONTINUE - 3: "))


def generate():
    del value[:]
    del weight[:]
    for i in range(8):
        value.append(random.randint(1, 500))
    for j in range(8):
        weight.append(random.randint(1, 500))


def reading():
    del value[:], weight[:]
    for i in file2.readline().split(','):
        value.append(int(i))
    for i in file2.readline().split(','):
        weight.append(int(i))


match r:
    case 1:
        generate()
        print("Random values generated.")
    case 2:
        reading()
        print("Values readed from file.")
    case 3:
        print("Continuing.")
    case _:
        print("Wrong answer.")
        quit()


q = len(value)


while True:
    capacity = int(input("Capacity: "))
    c = int(input("Which method you want to use? (1-B, 2-G, 3-D, 4 for quit): "))
    start = timer()
    file1.write("#another attempt\n")
    file1.write(str(q) + "\n")
    file1.writelines(str(value) + "\n")
    file1.writelines(str(weight) + "\n")
    file1.write(str(capacity) + "\n")
    method_Brute = brute(capacity, weight, value, q)
    method_Greed = round(greed.calculateTheValue(weight, value, capacity))
    method_Dynamic = dynamic(capacity, weight, value)

    match c:
        case 1:
            print("Max value for this capacity is: ", method_Brute)
            end = timer()
            print(end - start)
            file1.write("brute\n" + str(method_Brute) + "\n")

        case 2:
            print("Max value for this capacity is: ", method_Greed)
            end = timer()
            print(end - start)
            file1.write("greedy\n" + str(method_Greed) + "\n")

        case 3:
            print("Max value for this capacity is:", method_Dynamic)
            end = timer()
            print(end - start)
            file1.write("dynamic\n" + str(method_Dynamic) + "\n")

        case 4:
            print("Quitted.")
            quit()

        case _:
            print("Wrong answer.")
            quit()

file1.write("\n")
file1.close()
file2.close()
