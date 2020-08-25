# Heron's Formula for the area of a triangle
# Area = (p(p − a)(p − b)(p	− c))^1/2
# p = (a + b + c)/2
import math
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    s = a+b+c
    p = (a + b + c)/2
    area = int(math.sqrt(p*(p-a)*(p-b)*(p-c)))
    print(area == s)