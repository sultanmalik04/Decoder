a, b = map(int, input().split())
if 11 in [a,b]:
    s = a + b - 10
else:
    s = a + b
print(s if s <= 21 else 0)