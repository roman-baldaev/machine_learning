import points
import random
import matplotlib.pyplot as plt

a = points.Points(4)
print(a._colors)

print(a._color_part)
number = 100

for i in range(4):
    k = random.uniform(-100,100)
    print(k)
    a.add_points(i, [random.uniform(0, i + k) for i in range(number)], [random.uniform(0, i + k) for i in range(number)])
a.show_sets()