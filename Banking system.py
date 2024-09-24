initial_amount = 1000
print('Hy! we have these three option which you want to choose?')
print('1_withdraw')
print('2_deposit')
print('3_check balance')
option = str(input('Enter Your option:'))
if option == 'withdraw':
    amount = int(input('Enter amount:'))
    if initial_amount < amount:
        print('Sorry!You Entered Invalid data.please enter Valid Amount.')
    else:
        initial_amount = initial_amount - amount
        print('your withdraw amount is', amount)
        balance = str(input('you want you check your remaining  balance:'))
        if balance == 'yes':
            print('your bank balance is:', initial_amount)
        else:
            print('ok')
elif option == 'deposit':
    amount = int(input('Enter amount:'))
    initial_amount = initial_amount + amount
    print('your deposit amount is', amount)
    balance = str(input('you want to check your remaining balance:'))
    if balance == 'yes':
        print('your bank balance is:', initial_amount)
    else:
        print('Thanks you!')
elif option == 'check balance':
    print('your total balance is :', initial_amount)
else:
    print('Invalid option.please try again.')
