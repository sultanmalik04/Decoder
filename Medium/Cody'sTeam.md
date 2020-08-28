## Python

```python
    n, k = map(int, input().split())
    marks = list(map(int, input().split()))
    max_sum = 0
    for i in range(n-k+1):
        cur_sum = 0
        for j in range(k):
            cur_sum += marks[i+j]
        max_sum = max(cur_sum, max_sum)
    print(max_sum)
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
        int k = sc.nextInt();
        int marks[] = new int[n];
        for(int i = 0; i < n; i++){
            marks[i] = sc.nextInt();
        }
        int max_sum = Integer.MIN_VALUE;
        for(int i = 0; i < n-k+1; i++){
            int cur_sum = 0;
            for(int j = 0; j < k; j++){
                cur_sum += marks[i+j];
            }
            max_sum = max_sum < cur_sum ? cur_sum:    max_sum;
        }
        System.out.println(max_sum);
        }
}
```