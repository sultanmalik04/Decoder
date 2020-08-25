n = int(input())
c = input().split()
for i in range(n-1):
    for j in range(n-i-1):
        if ord(c[j].lower()) > ord(c[j+1].lower()):
            c[j], c[j+1] = c[j+1], c[j]
print(" ".join(c))
