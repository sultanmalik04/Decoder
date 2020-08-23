string = input()
result = [chr(ord(i) + 1) for i in string]
print(*result, sep='')