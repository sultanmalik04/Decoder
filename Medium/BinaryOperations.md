We only have to define a function for addition...\
We can use the logic of repitative addition for multiplication...\
So we don't have define a function for multiplication...\
We can do the addition bit by bit...



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

## Java
```java
import java.util.*;

//Compiler version JDK 11.0.2
class Solution {
    public String binaryAdd(String a, String b) {
        StringBuilder result = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        while (i >= 0 || j >= 0){
            int sum = carry;
            if (i >= 0) sum += a.charAt(i--) - '0';
  	    if (j >= 0) sum += b.charAt(j--) - '0';
            result.append(sum % 2);
            carry = sum / 2;
        }
        if (carry != 0) 
            result.append(carry);
            
        return result.reverse().toString();
    }
}

class Dcoder
{  
  public static void main(String args[])
  {  
    //System.out.println("Hello, Dcoder!");
      Scanner sc = new Scanner(System.in);
      String []s= sc.nextLine().split(" ");
      String a = s[0], b = s[1];
      Solution obj = new Solution();
      System.out.println(obj.binaryAdd(a,b));
      int i = b.length() - 1, j = 0;
      int int_b = 0;
      while (i >= 0)
        int_b += Math.pow(2,j++) * (b.charAt(i--) -    '0');
      String muliplication = "0";
      for (i = 0; i < int_b; i++){
          muliplication = obj.binaryAdd(a, muliplication);
      }
      System.out.println(muliplication);
  }
}
```