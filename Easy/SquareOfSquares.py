import math

n = int(input())
if n >= 0 and int(math.sqrt(n))**2 == n:
    print('YES')
else:
    print('NO')