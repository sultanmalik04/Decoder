


## Python
```python
    def binaryAdd(a,b):
        i, j = len(a)-1, len(b)-1
        carry = 0
        result = ''
        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum +=  int(a[i])
            if j >= 0:
                sum += int(b[j])
            result += str(sum%2)
            carry  = sum//2
            i -= 1
            j -= 1
        if carry > 0:
            result += str(carry)
        return result[::-1]
    
    a, b = input().split()
    print(binaryAdd(a,b))
    i = len(b)-1
    j = 0
    int_b = 0
    while i >= 0:
        int_b += 2**j * int(b[i])
        j += 1
        i -= 1
    multiplication = '0'
    for _ in range(int_b):
        multiplication = binaryAdd(a, multiplication)
    print(multiplication)
```