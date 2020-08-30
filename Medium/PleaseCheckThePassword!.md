
## Python
```python
    passwd_list = []
    for _ in range(int(input())):
        passwd_list.append(input())
    for i in passwd_list:
        if i[::-1] in passwd_list:
            password = i
            break
    l = len(password)
    print(l, password[l//2])
```

## Java
```java
```