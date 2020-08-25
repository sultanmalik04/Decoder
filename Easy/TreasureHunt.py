maxW = int(input())
value1, W1 = map(int, input().split())
value2, W2 = map(int, input().split())
result = 0
if W1 + W2 <= maxW:
    result = value1+value2
else:
    if value1 > value2:
        result = value1
    else:
        result = value2
print(result)
