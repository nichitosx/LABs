import time

# Определение декоратора
def logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции '{func.__name__}': {execution_time:.6f} секунд")
        return result
    return wrapper

# Две функции для применения декоратора
@logger
def calculate_sum(n):
    return sum(range(n))

@logger
def calculate_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Тестирование функций
print(calculate_sum(1000000))
print(calculate_factorial(1000))