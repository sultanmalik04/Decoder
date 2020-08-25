n = int(input())
s = input()
l = len(s)
for i in range(0,l-1,2):
    if s[i] == s[i+1]:
        print('Draw')
    elif s[i] == 'P' and s[i+1] == 'R':
        print('Dcoder')
    elif s[i] == 'R' and s[i+1] == 'P':
        print('You')
    elif s[i] == 'S' and s[i+1] == 'P':
        print('Dcoder')
    elif s[i] == 'P' and s[i+1] == 'S':
        print('You')
    elif s[i] == 'R' and s[i+1] == 'S':
        print('Dcoder')
    elif s[i] == 'S' and s[i+1] == 'R':
        print('You')
