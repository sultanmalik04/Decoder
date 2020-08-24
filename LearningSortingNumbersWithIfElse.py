m, n, p = map(int, input().split())
if m < n < p:
    print(m, n, p)
elif m < p < n:
    print(m, p, n)
elif p < m < n:
    print(m, p, n)
elif p < n < m:
    print(p, n, m)
elif n < p < m:
    print(n, p, m)
else:
    print(n, m, p)