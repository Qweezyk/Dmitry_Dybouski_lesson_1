prices = [57.8, 45.51, 59.54, 32.02, 49,99, 22, 29.9, 32, 54, 44]
prices_2 = []
new_prices = []

for price in prices:
    a = int(price)
    b = (price % int(price)) * 100
    b = int(round(b, 2))
    total_price = f'{a} руб. {b:02.0f} коп.'
    new_prices.append(total_price)
    total_price = None
prices_2.extend(new_prices)
print(new_prices)
print(f'id списка: {id(new_prices)}')
new_prices.sort()
print(new_prices)
print(f'id списка {id(new_prices)}')
prices_2.sort(reverse=True)
print(prices_2)
print(f'id списка: {id(prices_2)}')
print(f'Пять самых дорогих товаров по возрастанию: {prices_2[4::-1]}')

