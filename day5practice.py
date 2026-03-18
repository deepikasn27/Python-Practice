
# import csv
# print("script is running")
# with open('leads.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         if row[0] == 'name':
#             continue
#         # print(int(row[2]))
#         if int(row[2]) > 70:
#             print(row)


# try:

#     with open('leads.csv', 'r') as file:
#         with open('hot_leads.csv', 'w', newline='') as write_file:
#             reader = csv.reader(file)
#             writer = csv.writer(write_file)
#             writer.writerow(['name', 'source', 'score'])
#             for row in reader:
#                 if row[0] == 'name':
#                     continue
#                 if int(row[2]) > 70:
#                     print(row)
#                     writer.writerow(row)
# except FileNotFoundError:
#     print('File leads.csv was not found')

# try:
#     with open('sales.csv', 'r') as sales_file:
#         with open('big_sales.csv', 'a', newline='') as big_file:
#             reader = csv.reader(sales_file)
#             writer = csv.writer(big_file)
#             writer.writerow(['date', 'salesperson', 'amount'])
#             for row in reader:
#                 if row[0] == 'date':
#                     continue
#                 if int(row[2]) > 5000:
#                     print(row)
#                     writer.writerow(row)
# except FileNotFoundError:
#     print('File was not found')

# user = {'name': 'deepika', 'age': 50,
#         'occupation': 'musician', 'pet': 'baby elephant'}
# print(type(user))
# print(user.keys())
# print(user.values())
# print(user.items())
# for keys, values in user.items():
#     print(keys)
# user['name'] = 'Rayn'
# print(user)
# age = user.pop('age')
# print(age)
# print(user.pop('occupation'))
# print(user.popitem())
# user = dict.fromkeys(['name', 'age', 'occupatio', 'pet'], None)
# print(user)

# crm = {
#     'lead_1': {
#         'name': 'Priya',
#         'score': 85
#     },
#     'lead_2': {
#         'name': 'Ravi',
#         'score': 60
#     }
# }

# print(crm['lead_1'])
# print(crm['lead_1']['name'])

# crm = {
#     'lead_1': {
#         'name': 'rayn',
#         'score': 85
#     },
#     'lead_2': {
#         'name': 'deepika',
#         'score': 89
#     }
# }
# print(crm['lead_1']['name'])

contacts = {
    'Rayn': {
        'Phone': '9978867090',
        'Email': 'rayn@gmail.com',
        'City': 'London'
    },
    'Deepika': {
        'Phone': '9090908985',
        'Email': 'deepika@gmail.com',
        'City': 'Stockholm'
    },
    'Sacha': {
        'Phone': '8887884335',
        'Email': 'sacha@gmail.com',
        'City': 'New York'
    }
}
print(contacts.keys())
print(contacts['Sacha'])
contacts['Rayn']['City'] = 'Austria'
print(contacts)
for keys, City in contacts.items():
    print(keys, City)
contacts['Naira'] = {
    'Phone': '9861765655',
    'Email': 'naira@gmail.com',
    'City': 'London'}
print(contacts)
for keys, values in contacts.items():
    print(keys)
for name, details in contacts.items():
    print(name, details['City'])
