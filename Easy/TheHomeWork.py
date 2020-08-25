for _ in range(int(input())):
    k = int(input())
    digits = list(map(int, input().split()))
    digits.sort()
    digits.reverse()
    print(*digits, sep='')
