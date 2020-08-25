def gcd(n, d):
    while d:
        n, d = d, n % d
    return n

n, d = map(int, input().split())
g = gcd(n, d)
print(n//g, d//g)
