n = input()
l = len(n)
res = str(int('1'*l) - int(n))  # subtract the given number from 11111111... of length len(n)
                                # as 1 - 1 = 0 and 1 - 0 = 1
print('0'*(l-len(res))+res)     # in final result add required number of 0 before the res
