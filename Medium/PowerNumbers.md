## Python
```python
n = int(input())
arr = list(map(int, input().split()))
pow_numbers = [i**i for i in range(1, 16)]
result = ['Yes' if i in pow_numbers else 'No' for i in arr]
print(*result)
```
## Java
```java
    import java.util.*;

    //Compiler version JDK 11.0.2

    class Dcoder
    {  
      public static void main(String args[])
      {
          Scanner sc = new Scanner(System.in);
          int n = sc.nextInt();
          long arr[] = new long[n];
          for (int i = 0; i < n; i++) 
              arr[i] = sc.nextLong();
          List<Long> pow_numbers = new ArrayList<Long>();
          for (int i = 1; i < 16; i++) 
              pow_numbers.add((long)Math.pow(i,i));
          for (int i = 0; i < n; i++){
              if (pow_numbers.contains(arr[i])) 
                  System.out.print("Yes ");
              else
                  System.out.print("No ");
          }
      }
    }
```