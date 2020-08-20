A, M, N, D = map(int, input().split())
print((M*A + (D-A)*N) if D > A else M*D)
