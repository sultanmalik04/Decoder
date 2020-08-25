years = [int(input()) for _ in range(int(input()))]
result = ["Yes" if (y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)) else "No" for y in years]
for i in result:
    print(i)
