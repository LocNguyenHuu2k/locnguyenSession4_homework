prices = {}

prices['banana'] = 4
prices["apple"] =  2
prices["orange"] = 1.5
prices["pear"] = 3
#
# for key, value in prices.items():
#     print(key,':',value)

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for i in range(5):
    if i % 2 != 0:
        print(i)

for key_prices, value_prices in prices.items() :
    print(key_prices)
    for key_stocks, value_stocks in stock.items():
        if key_stocks == key_prices :
            print("prices: ",value_prices)
            print("stock: ",value_stocks)

total = 0

for key_prices ,value_prices in prices.items():
    for key_stocks, value_stocks in stock.items():
        if key_stocks == key_prices:
            money = value_prices* value_stocks
            print(money)
            total += money

print(total)