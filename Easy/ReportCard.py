marks = map(int, input().split())
mean_score = sum(marks)/3
if mean_score > 90 and mean_score <= 100:
    print('A')
elif mean_score > 80 and mean_score <= 90:
    print('B')
elif mean_score > 70 and mean_score <= 80:
    print('C')
elif mean_score > 60 and mean_score <= 70:
    print('D')
elif mean_score <= 60:
    print('F')
