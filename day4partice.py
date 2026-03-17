def greet(name):
    full_name = name.strip().title()
    return (f'Hello {full_name}, welcome to AI world!')


print(greet('Rayn'))
print(greet('Jeh'))
print(greet('Naina'))


# Write a function called calculate_bill
def calculation_bill(price, quantity, tax_rate):
    total_price = price*quantity
    final_price = total_price + (total_price*tax_rate)
    return (round(final_price, 2))


print(calculation_bill(500, 3, 0.18))
print(calculation_bill(1200, 2, 0.05))


# Write a function called make_coffee
def make_coffee(size, sugar=1, milk=True):

    return f'Your {size} coffee with {sugar} sugar(s) and {'milk' if milk else 'no milk'}'


print(make_coffee('large'))
print(make_coffee('small', sugar=0))
print(make_coffee('medium', sugar=2, milk=False))


def validate_email(email):
    if '@' in email and email.endswith('.com') and email.strip():
        return True
    else:
        return False


print(validate_email('deepika.nagrah@gmail.com'))


def register_user(name, email):
    if validate_email(email):
        return (f'Welcome {name}! Registration successful.')
    else:
        return (f'Registration failed. Invalid email.')


print(register_user('Deepika', 'deepika@gmail.com'))
print(register_user('Rahul', 'rahulgmail.com'))
print(register_user('Anita', 'anita@yahoo.co.uk'))


def sales_list(sales):
    days = len(sales)
    total = sum(sales)
    average = round(total/days)
    highest = max(sales)
    lowest = min(sales)
    return f'total: {total}, average: {average}, highest: {highest}, lowest: {lowest}, days: {days}'


print(sales_list([12500, 8900, 15200, 6700, 19800, 11200, 9400]))


def sales_list(sales):
    days = len(sales)
    total = sum(sales)
    average = round(total/days)
    highest = max(sales)
    lowest = min(sales)
    return {
        'total': total,
        'average': round(total/days, 2),
        'highest': highest,
        'lowest': lowest,
        'days': days
    }


result = sales_list([12500, 8900, 15200, 6700, 19800, 11200, 9400])
print(result['total'])
print(result['average'])
print(result['highest'])
print(result['lowest'])
print(result['days'])
