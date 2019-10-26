import math
i = 1
highSq = 0
while i < 1000:
    sqrt = math.sqrt(i)
    if sqrt > highSq:
        print(sqrt)
    elif type(sqrt) is int:
        highSq = sqrt
    i += 1
print(highSq)