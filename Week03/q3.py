point1 = (3,5)
point2 = (7,2)
print(f"x1 = {point1[0]}, y1 = {point1[1]}")
print(f"x2 = {point2[0]}, y2 = {point2[1]}")

x1,y1 = point1
x2,y2 = point2

print(f"Distance between points: {((x2-x1)**2 + (y2-y1)**2)**0.5}")
temp = tuple("PYTHON")
print(f"Characters tuple {temp}")
for char in temp:
    print(char)