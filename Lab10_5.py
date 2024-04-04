class ValueTooLargeError(Exception):
    def __init__(self, value, threshold):
        self.value = value
        self.threshold = threshold

    def __str__(self):
        return f"Значение {self.value} превышает порог {self.threshold}"

def check_value(value):
    threshold = 100
    if value > threshold:
        raise ValueTooLargeError(value, threshold)
    else:
        print("Значение находится в пределах допустимого порога.")

try:
    check_value(120)
except ValueTooLargeError as e:
    print("Ошибка:", e)

def process_data(data):
    max_threshold = 10
    for value in data:
        if value > max_threshold:
            raise ValueTooLargeError(value, max_threshold)

data = [5, 12, 3, 8, 15]
try:
    process_data(data)
except ValueTooLargeError as e:
    print("Ошибка:", e)