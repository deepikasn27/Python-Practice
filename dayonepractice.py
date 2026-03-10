print("===== YOUR PROFILE =====")
name = 'Deepika'
age = 25
city = 'Bangalore'
annual_salary = 300000.0
can_vote = True
is_senior = (age > 30)
name_lenghth = len(name)
print(f'Name: {name} \nAge: {age} \nCity: {city} \nAnnual salary:{annual_salary} \nCan vote: {can_vote} \nIs senior: {is_senior} \nName lenghth: {name_lenghth}')
print("========================")


# Unit converter

weight = float(input('Enter your weight : '))
unit = input('Enter wether your weight is in Kilograms or Pounds(K Or L): ')

if unit == 'K':
    weight = round(weight * 2.205)
    unit = 'L'
    print(f'Your weight in Pounds: {weight}{unit}')

elif unit == "L":
    weight = round(weight/2.205)
    unit = 'K'
    print(f'Your weight in Kilograms: {weight}{unit}')

else:
    print('Invalid input')


# exercise 2

distance = float(input('Enter the distance :'))
unit = input("Enter wether the distance is in Kilometers or Miles(Km Or Mi) : ")

if unit == 'Km':
    distance = round(distance * 0.621)
    unit = 'Mi'
    print(f'The distance in Miles : {distance} {unit}')
elif unit == 'Mi':
    distance = round(distance / 0.621)
    unit = 'Km'
    print(f'The distance in Kilometers : {distance} {unit}')
else:
    print('Invalid input')


# exercise 3

amount = float(input('Enter the amount : '))
currency = input(
    'Enter wether your currency is in Rupees or Dollars( R or D) : ')

if currency == 'R':
    amount = round(amount*0.011, 2)
    currency = 'Dollars'
    print(f'The amount in dollars is {amount}{currency}')
elif currency == 'D':
    amount = round(amount/0.011, 2)
    currency = 'Rupees'
    print(f'The amount in rupees is {amount}{currency}')
