n = int(input())
inp = input().split()
dic = {}
for i in inp:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
for i in result:
    print(i[0], end=' ')
