import re
T = int(input())
for _ in range(T):
    string, sub_str = input().split()
    if sub_str in string:
        print("Yes")
    else:
        print("No")