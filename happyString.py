
n = int(input())
s = 'a'
result = [chr(ord(s)+i) for i in range(n)]
print("".join(result[::-1]))
