value = []
weight = []
file2 = open("values.txt", "r")


def reading():
    del value[:]
    del weight[:]
    v_read = file2.readline()
    for i in v_read:
        for j in i.split(','):
            value.append(j)
    w_read = file2.readline()
    for i in w_read:
        for j in i.split(','):
            weight.append(j)


reading()


q = len(value)

print(value)
print(weight)
print(q)
file2.close()
