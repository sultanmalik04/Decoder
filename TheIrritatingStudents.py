for _ in range(int(input())):
    n = int(input())
    print(*[n//2, n//2 + 1] if n % 2 else [n//2, n//2])