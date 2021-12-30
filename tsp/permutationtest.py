# https://docs.python.org/3/library/itertools.html
import itertools

path = [0, 1, 2, 3, 0]

print(path[1:-1])
permutated = itertools.permutations(path[1:-1], len(path) - 2)
for i in permutated:
    print(i)

# I need to call it once more, because itertools was once iterated
permutated = itertools.permutations(path[1:-1], len(path) - 2)
# now you can loop coping permutated values to new list
for i in permutated:
    new_path = [0]
    new_path.extend(i)
    new_path.append(0)
    print(new_path)
    # now you can count values for all paths, or anything you want
    sum = 0
    for j in new_path:
        sum += j
    print(sum)
