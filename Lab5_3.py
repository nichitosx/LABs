one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

one_max = max(one)
one_min = min(one)
two_max = max(two)
two_min = min(two)
three_max = max(three)
three_min = min(three)

def triangle_area(a, b, c):
    p = (a + b + c) / 2
    if p <= max(a, b, c) / 2:
        return 0
    else:
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

max_area = max(triangle_area(one_max, two_max, three_max), triangle_area(one_min, two_min, three_min))
min_area = min(triangle_area(one_max, two_max, three_max), triangle_area(one_min, two_min, three_min))

print("Площадь треугольника с максимальными сторонами:", max_area)
print("Площадь треугольника с минимальными сторонами:", min_area)