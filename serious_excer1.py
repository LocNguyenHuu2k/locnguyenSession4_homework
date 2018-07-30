inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print('     INVENTORY')
for key, value in inventory.items():
    print(key,':',value)

print('     ADD POCKET TO INVENTORY')
inventory['pocket'] = ['sea shell','strange berry','lint']

for key, value in inventory.items():
    print(key,':',value)

print('     REMOVE DAGGER FROM BACK PACK')
inventory['backpack'].remove('dagger')

for key, value in inventory.items():
    print(key,':',value)

inventory['gold'] += 50
print('     ADD 50 GOLD TO INVENTORY ')


for key, value in inventory.items():
    print(key,':',value)



