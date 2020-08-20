for _ in range(int(input())):
    n, m = map(int, input().split())
    print('Yes' if m % n == 0 else 'No')