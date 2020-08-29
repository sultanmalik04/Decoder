## Python
```python
    import math as m

    for _ in range(int(input())):
        n = int(input())
        print(round(m.sqrt(n)))
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
         int T = sc.nextInt();
            for (int i = 0; i < T; i++){
                int n = sc.nextInt();
                System.out.println(Math.round(Math.sqrt(n)));
            }
        } 
    }
```