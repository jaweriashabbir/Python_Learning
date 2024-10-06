print('Hey!we have three services.which you want to do?')
print('Enter a for weight lose ,Enter b for weight gain , Enter c for staying at same weight ')
services = str(input('Enter any service:'))
print('please Enter some basic information.')
weight = int(input('Enter your weight:'))
height = int(input('Enter your height in cm:'))
age = int(input('Enter your age:'))
Gender = (input('Enter your Gender:'))
calories = 0
if services == 'a':
    if Gender == 'male':
        calories = ((10 * weight) + (6.25 * height) - (5 * age) + 5)
    elif Gender == 'female':
        calories = ((10 * weight) + (6.25 * height) - (5 * age) - 161)
    print('you should take less than ', calories, 'calories in per day.')
elif services == 'b':
    if Gender == 'male':
        calories = ((10 * weight) + (6.25 * height) - (5 * age) + 5)
    elif Gender == 'female':
        calories = ((10 * weight) + (6.25 * height) - (5 * age) - 161)
    print('you need more than ', calories, 'calories in per day.')
elif services == 'c':
    if Gender == 'male':
        calories = ((10 * weight) + (6.25 * height) - (5 * age) + 5)
        print('you have to take', calories, 'calories in per day.')
    elif Gender == 'female':
        calories = ((10 * weight) + (6.25 * height) - (5 * age) - 161)
    print('you have to take', calories, 'calories in per day.')
else:
    print('Invalid service.')




