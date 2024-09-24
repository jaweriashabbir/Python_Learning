total_price = int(input('Enter your total glossary price:'))
print('type yes if you are member of store ,otherwise type no.')
membership = input('Are you member of store? ')
discount = 0
discount_formula = 0
if total_price <= 100:
    discount = 0
elif total_price > 100 and total_price <= 200:
    discount = discount + 2
if total_price > 200 and total_price <= 300:
    discount = discount + 5
if total_price > 300 and total_price <= 500:
    discount = discount + 8
elif total_price > 500:
    discount = discount + 15

if membership == 'yes':
    discount += 5
discount_formula = (total_price -(total_price * discount/100))
print('your Discount is', discount, 'and your amount is', discount_formula)



