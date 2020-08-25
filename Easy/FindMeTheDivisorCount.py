l, h, d = map(int, input().split())
print(sum([1 for i in range(l, h+1) if i % d == 0]))