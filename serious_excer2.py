prices = {}

prices['banana'] = 4
prices["apple"] =  2
prices["orange"] = 1.5
prices["pear"] = 3

print('   PRICES ')

for key, value in prices.items():
    print(key,':',value)

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

print('   STOCK ')
for key, value in stock.items():
    print(key,':',value)

print('  INFORMATION ')

i = 0

for key_prices, value_prices in prices.items() :
    i += 1
    print( i,'.',key_prices)
    for key_stocks, value_stocks in stock.items():
        if key_stocks == key_prices :
            print("prices: ",value_prices)
            print("stock: ",value_stocks)

total = 0

print('   TOTAL MONEY')
for key_prices ,value_prices in prices.items():
    for key_stocks, value_stocks in stock.items():
        if key_stocks == key_prices:
            money = value_prices* value_stocks
            print(key_stocks,':',money)
            total += money

print( 'Total money =',total)