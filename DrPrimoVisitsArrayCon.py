n = int(input())
arr = list(map(int, input().split()))
count = 0
m = max(arr)
isprime = [None]*(m+1)

for i in range(m+1):
    isprime[i] = True
isprime[0], isprime[1] = False, False
for i in range(2, m+1):
    if isprime[i] == True:
        for j in range(i*i, m+1, i):
            isprime[j] = False

for i in arr:
    if isprime[i] == True:
        count += 1
print(count)
