for _ in range(int(input())):
    M, A = map(int, input().split())
    print('Pass' if M > 70 and A > 50 else 'Fail')