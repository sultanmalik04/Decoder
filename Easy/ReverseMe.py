n = int(input())
rev_no = 0
while n:
    rev_no = rev_no*10 + n % 10
    n //= 10
print(rev_no)