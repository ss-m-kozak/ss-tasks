def max_sum_dividers():
    sums = {}
    for i in range(1, 10000):
        sums[i] = 0
    
        for j in range(1, i + 1):
            if i % j == 0:
                sums[i] += j
    
    return max(sums, key=sums.get)

print(max_sum_dividers())