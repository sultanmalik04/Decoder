for _ in range(int(input())):
    cost = int(input())
    if cost > 1000:
        print("{0:.2f}".format(cost - cost*10/100))
    else:
        print("{0:.2f}".format(cost))