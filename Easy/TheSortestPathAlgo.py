# Using distance formula
# d = sqrt{(x_2 - x_1)^2 + (y_2-y_1)^2}
# for origin x1 = 0 and y1 = 0

x1, y1, x2, y2 = map(int, input().split())
x_distance = (x1**2 + y1**2)**0.5
y_distance = (x2**2 + y2**2)**0.5
print('A' if x_distance < y_distance else 'B')