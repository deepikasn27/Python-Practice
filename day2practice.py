# validtae the quality and correctness of password
password = input('Enter password:')
email = input('Enter email:')
has_upper = False
has_lower = False

if password == '':
    print('Password must not be empty')
if len(password) < 8:
    print('password must be at least 8 characters')
for character in password:
    if character.isupper():
        has_upper = True
for character in password:
    if character.islower():
        has_lower = True
if not has_upper:
    print('Password must contain at least one uppercase')
if not has_lower:
    print('Password must contain at least one lowercase')
if password == email:
    print('Password cant not be same as email')
if ' ' in password:
    print('password must not contain any spaces')
if not (password[0].isalnum() and password[-1].isalnum()):
    print('Password must start and end with an aplhabet or number')

    # LISTS PRACTICE
    guests = ['deepika', 'sejal', 'rakshitha',
              'aishwarya', 'pragati', 'varshana']
guests[0] = 'Hamamura'
print('deepika can not make it to the dinner hence place is replace by Hamamura')
guests[3] = 'yokashaki'
print('aishwarya can not make it to the dinner hence place is replaced by yokashaki')
for guest in guests:
    print(f'Dear {guest}, you are invited to our dinner!')


guests.insert(0, 'Anusha'), guests.insert(4, 'Kamala'), guests.append('Siya')
print(guests)
for guest in guests:
    print(f'Dear {guest}, you are invited to our dinner!')


print('sorry, I can invite only two people for dinner.')
popped_guests = guests.pop(0)
print(f'Sorry {popped_guests}, you are not invited to our dinner!')
popped_guests = guests.pop(4)
print(f'Sorry {popped_guests}, you are not invited to our dinner!')
popped_guests = guests.pop(3)
print(f'Sorry {popped_guests}, you are not invited to our dinner!')
popped_guests = guests.pop(5)
print(f'Sorry {popped_guests}, you are not invited to our dinner!')
popped_guests = guests.pop(1)
print(f'Sorry {popped_guests}, you are not invited to our dinner!')
popped_guests = guests.pop(2)
print(f'Sorry {popped_guests}, you are not invited to our dinner!')
popped_guests = guests.pop(-1)
print(f'Sorry {popped_guests}, you are not invited to our dinner!')
print(f'invited guests{guests}')
for guest in guests:
    print(f'Dear {guest}, you are still invited to our dinner!')
guests.remove('Hamamura'), guests.remove('rakshitha')
print(guests)

# working with lists

locations = ['New York', 'London', 'Sweden', 'Scotland', 'Norway', 'Italy']
for location in locations:
    print(location)

print(sorted(locations))

print(locations)

locations.reverse()
print(locations)

locations.reverse()
print(locations)

locations.sort()
print(locations)

locations.sort(reverse=True)
print(locations)

guests = ['deepika', 'sejal', 'rakshitha', 'aishwarya', 'pragati', 'varshana']
for guest in guests:
    print(f'{guest.upper()},you suck\n')

pizzas = ['go pizza', 'dominos', 'pizza hut']
for pizza in pizzas:
    print(f'I love {pizza.title()} so much')
print('I really love pizza')

tables_7 = [value*7 for value in range(1, 11)]
print(f'{tables_7}')
