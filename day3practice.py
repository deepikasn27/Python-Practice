
# Exercise 1
import random
text = "   Python Programming is POWERFUL   "
cleaned = text.strip().lower().replace('powerful', 'awesome')
print(cleaned)
print(f'Number of characters: {len(cleaned)}')
print(cleaned.startswith('python'))
print('programming' in cleaned)

# Exercise 2
sentence = "Machine Learning is transforming the world"
print(sentence[:8])
print(sentence[-5:])
print(sentence[::2])
print(sentence[::-1])
print(sentence[8:16])

# Exercise 3
username = "Deepika123"
print(username.isalpha())
print(username.isalnum())
print(username.upper())
print(username.count('e'))

# Exercise 4
name = "Deepika"
age = 22
city = "Bangalore"
print(f'My name is {name}. I am {age} years old and live in {city}.')

# Exercise 5 — String Operators

word = "AI"
print(word*5)
print(word + ' ' 'Revolution')

# Exercise 6
price = 850
quantity = 6
tax = 0.18
total_price = price*quantity
print(f'Total: {total_price}')
tax_amount = total_price*tax
print(f'Tax amount: {tax_amount}')
final_price = total_price+tax_amount
print(f'Final amount: {round(final_price, 3)}')

# Exercise 7
a = 25
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)

# Exercise 8
print(random.random()*10)
print(random.randint(1, 10))
print(random.randint(50, 100))

# Exercise 9
value = 45.8
print(type(value))
print(isinstance(value, int))
print(value.is_integer())

# Exercise 10
marks = 72
if marks >= 75:
    print('Distinction')
elif marks >= 60:
    print('First Class')
elif marks >= 40:
    print('Pass')
else:
    print('Fail')

# Bonus Exercise
number = 17
if number % 2 == 0:
    print(f'{number} is Even')
else:
    print(f'{number} is Odd')

# Exercise 11
age = 22
has_id = True
if (age == 21 or age > 21) and has_id:
    print('Entry Allowed')
else:
    print('Entry denied')

# Exercise 12
skills = ["python", "excel", "powerbi"]
print('python' in skills)
print('tableau'not in skills)

# Exercise 13
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a == b)
print(a is b)
print(a is c)

# Exercise 14
age = 19
has_ticket = True
is_student = True
if (age >= 18 and has_ticket) or is_student:
    print('Entry allowed')
else:
    print('Entry denied')

# Exercise 15
temperature = 32
raining = True
if temperature > 30:
    if raining:
        print('Hot but raining')
    else:
        print('Hot and sunny')
else:
    print("Weather is normal")

# Exercise 17
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)
for number in range(1, 11):
    print(number)

# Exercise 18
for number in range(1, 11):
    if number == 5:
        continue
    print(number)

# Exercise 19
for number in range(1, 11):
    if number == 7:
        break
    print(number)

# Exercise 20
for star in range(1, 7):
    print('*' * star)

# Exercise 21,22&23
numbers = [12, 45, 67, 23, 89]
print(numbers[0])
print(numbers[4])
print(numbers[0:3])
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))
print(45 in numbers)
print(numbers.count(23))
print(numbers.index(67))

# Exercise 24
fruits = ["apple", "banana", "mango"]
fruits.append('orange')
fruits.insert(1, 'grapes')
fruits.remove('banana')
print(fruits)

# Exercise 25
numbers = [8, 3, 12, 1, 5]
print(sorted(numbers))
print(sorted(numbers, reverse=True))

# Exercise 26
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(data[1][1])
print(data[2][2])

# Exercise 27
numbers = [2, 4, 6, 8]
if all(num % 2 == 0 for num in numbers):
    print('All numbers are even')


# Exercise 28
numbers = [1, 3, 5, 6]
if any(num % 2 == 0 for num in numbers):
    print('TRUE')

# Exercise 29
numbers = [1, 2, 3]
numbers = [1, 2, 3]
new_list = [*numbers, 4, 5, 6]
print(new_list)

# Exercise 30
numbers = [10, 20, 30, 40]
numbers[2] = 35
print(numbers)

# Final Exercise

users = ["  deepika ", "rahul", "ANITA"]
scores = [72, 88, 55]
clean_users = [user.strip().capitalize() for user in users]
print(clean_users)
