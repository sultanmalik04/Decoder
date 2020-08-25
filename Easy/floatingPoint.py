T = int(input())
nums = []
for i in range(T):
    nums.append(float(input()))
    
for i in nums:
    print("{0:.2f}".format(i))