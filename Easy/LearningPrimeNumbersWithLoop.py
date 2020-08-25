m, n = map(int, input().split())
isprime = [None] * (n+1)
for i in range(n+1):
    isprime[i] = True
isprime[0], isprime[1] = False, False
for i in range(2, n+1):
    if isprime[i] == True:
        for j in range(i*i, n+1, i):
            isprime[j] = False
for i in range(m, n+1):
    if isprime[i] == True:
        print(i)