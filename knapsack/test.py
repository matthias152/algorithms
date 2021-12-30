# old
def reading():
    print("########old for debug start########")
    del value[:]
    del weight[:]
    v_read = file2.readline()
    print("How read line looks like?: " + v_read)
    for i in v_read:
        print("How i in read line looks like?: " + i)
        for j in i.split(','):
            # print("How j in read line looks like?: " + j)
            value.append(j)
    w_read = file2.readline()
    for i in w_read:
        for j in i.split(','):
            weight.append(j)
    print("########old for debug end########")


# new
def reading2():
    del value[:]
    del weight[:]
    v_read = file2.readline()           # its first line of file, so "20, 30, 40, 80, 100, 160, 250, 420"
    for i in v_read.split(','):         # you need to split read line by delimiter ',', so i will be 20 in first loop, 30 next etc.
        value.append(int(i))            # put i in value[]
    w_read = file2.readline()           # read next line of file, so "5, 10, 20, 45, 55, 144, 150, 220"
    for i in w_read.split(','):         # same as for value
        weight.append(int(i))           #


# better
def reading3():
    del value[:], weight[:]
    current_line = file2.readline()     # it does not matter if its v_read or w_read, because you are just using it once
    for i in current_line.split(','):   # so it could be just current_line
        value.append(int(i))            # rest is the same
    current_line = file2.readline()
    for i in current_line.split(','):
        weight.append(int(i))


# even better
def reading4():
    del value[:], weight[:]
    for i in file2.readline().split(','):
        value.append(int(i))
    for i in file2.readline().split(','):
        weight.append(int(i))


def print_all():
    print(value)
    print(weight)
    print(q)


value = []
weight = []
q = 0

file2 = open("values.txt", "r")
reading()
q = len(value)
print_all()
file2.close()

file2 = open("values.txt", "r")
reading2()
q = len(value)
print_all()
file2.close()

file2 = open("values.txt", "r")
reading3()
q = len(value)
print_all()
file2.close()

file2 = open("values.txt", "r")
reading4()
q = len(value)
print_all()
file2.close()
