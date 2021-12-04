sandwich_orders = ['Normal Chicken Sandwich','pastarami',
    'Fish Sandwich','pastarami','Ham Sandwich','pastarami','Veg Sandwich']
if 'pastarami' in sandwich_orders:
    print('Sorry,we are out of pastarami.')
while 'pastarami' in sandwich_orders:
    sandwich_orders.remove('pastarami')
print(sandwich_orders)
finished_sandwich = []
while sandwich_orders:
    making_sandwich = sandwich_orders.pop()
    print('Making Sandwich :' + making_sandwich)
    finished_sandwich.append(making_sandwich)

print('\nThe following sandwiches have been made : ')
for finished_sandwich in finished_sandwich:
    print(finished_sandwich)

