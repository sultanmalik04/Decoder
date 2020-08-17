n = int(input())
arr = list(map(int, input().split()))
print('Yes'if sum([1 for i in arr if i > 0]) == n else 'No')