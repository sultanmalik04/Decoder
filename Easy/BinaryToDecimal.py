n = input()
i = 0
j = len(n)-1
result = 0
while j >= 0:
    result += int(n[j]) * 2**i
    i += 1
    j -= 1
print(result)