for _ in range(int(input())):
    N = int(input())
    res = N % 10
    while N >= 10:
        N //= 10
    print(res+N)

# Alternate way of doing this Problem in Python
for _ in range(int(input())):
    N = input()
    print(int(N[0]) + int(N[-1]))
