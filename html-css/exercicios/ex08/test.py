prices = {'apple': 0.40, 'banana':0.50}
purchase = {
    'apple': 1,
    'banana': 6
}
bill = sum(prices[fruit] * purchase[fruit] for fruit in purchase)

print('I owe the grocer $%.2f' % bill)
print(len(purchase) == len(prices))