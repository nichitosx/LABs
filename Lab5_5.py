def transform_duplicates(numbers):
    result = set()
    duplicates = {}

    for num in numbers:
        if num not in duplicates:
            duplicates[num] = 1
        else:
            duplicates[num] += 1

        for i in range(1, duplicates[num] + 1):
            result.add(str(num) * i)

    return result


list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

print(transform_duplicates(list_1))
print(transform_duplicates(list_2))
print(transform_duplicates(list_3))