# We have to find the smallest number which when multiplied to N makes it a multiple of M. 

for _ in range(int(input())):
    n, m = map(int, input().split())
    n2 = m                    
    while n2:         
        n, n2 = n2, n % n2   # in the end n will contain GCD of n and m
    print(m//n)
