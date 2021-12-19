def brute(capacity, weight, value, q):
    if q == 0 or capacity == 0:
       return 0
    if (weight[q - 1] > capacity):
       return brute(capacity, weight, value, q - 1)
    else:
       return max(value[q-1] + brute(capacity-weight[q-1], weight, value, q-1),
       brute(capacity, weight, value, q-1))
