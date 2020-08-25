n = int(input())
if n >= 0:
    result = [2**i for i in range(n+1)]
else:
    result = [float(2**i) for i in range(n, 1)]
print(*result, sep=',')
