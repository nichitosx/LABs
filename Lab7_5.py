with open('Zadanie5.txt', 'r') as file:
    lines = file.readlines()

total_sales = 0
products = []

for line in lines:
    parts = line.split()
    product, price, quantity = parts[0], int(parts[1]), int(parts[2])
    total_sales += price * quantity
    products.append((product, price * quantity))

max_sales_product = max(products, key=lambda x: x[1])[0]
min_sales_product = min(products, key=lambda x: x[1])[0]

sorted_products = sorted(products, key=lambda x: x[0])

print("Общая сумма продаж:", total_sales)
print("Товар с наибольшей выручкой:", max_sales_product)
print("Товар с наименьшей выручкой:", min_sales_product)
print("Список всех товаров:")
for product, sales in sorted_products:
    print(product, "-", sales)