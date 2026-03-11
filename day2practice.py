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
if not (password.isalpha() and password.isnumeric()):
    print('Password must conatin only alphabets and numercis')
