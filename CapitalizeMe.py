string = input().split()
string = [i.capitalize() for i in string]
print(*string, sep=' ')