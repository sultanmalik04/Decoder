n = int(input())
arr = list(map(int, input().split()))
res = [arr[i] for i in range(1, n, 2) if arr[i] % 2 == 0]
print(*res, sep=' ')