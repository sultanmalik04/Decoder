n = int(input())
s = input()
result = [s[i] for i in range(len(s)) if s[i].isdigit()]
print(" ".join(result))
