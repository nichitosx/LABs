def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)

if __name__ == "__main__":
    values = tuple(map(float, input("Введите значения через пробел: ").split()))
    result = average(*values)
    print("Среднее арифметическое:", result)