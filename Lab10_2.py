try:
    with open('empty_file.txt', 'r') as file:
        data = file.read()
        if not data:
            raise Exception("Файл пустой")
        else:
            print("Содержимое файла 'empty_file.txt':")
            print(data)
except Exception as e:
    print(e)

print()

try:
    with open('not_empty_file.txt', 'r') as file:
        data = file.read()
        if not data:
            raise Exception("Файл пустой")
        else:
            print("Содержимое файла 'non_empty_file.txt':")
            print(data)
except Exception as e:
    print(e)