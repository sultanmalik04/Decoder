n = int(input())
s = input()
index = list(map(int, input().split()))
S = [s[i].swapcase() if i in index else s[i] for i in range(n)]
print("".join(S))