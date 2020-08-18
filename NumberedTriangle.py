n = int(input())
l = list(range(1, n+1))
for i in range(n):
    print(*l[0:i+1] , sep=" ")
