for _ in range(int(input())):
    angles = list(map(int, input().split()))
    if sum(angles) == 360:
        print('YES')
    else:
        print('NO')
