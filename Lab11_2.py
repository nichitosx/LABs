def fib():
    fib1, fib2 = 1, 1
    yield fib1
    yield fib2
    count = 2
    while True:
        fib1, fib2 = fib2, fib1 + fib2
        count += 1
        yield fib2

fibonacci_generator = fib()

while True:
    current_fib = next(fibonacci_generator)
    if current_fib >= 200:
        print(current_fib, end=' ')
        break

with open("fib.txt", "w") as file:
    file.write(str(current_fib) + "\n")

for _ in range(19):
    current_fib = next(fibonacci_generator)
    print(current_fib, end=' ')
    with open("fib.txt", "a") as file:
        file.write(str(current_fib) + "\n")
