leads = {
    'Rayn': {
        'Phone': '9978867090',
        'Email': 'rayn@gmail.com',
        'Source': 'Instagram',
        'Status': 'Interested'
    },
    'Deepika': {
        'Phone': '9090908985',
        'Email': 'deepika@gmail.com',
        'Source': 'LinkedIn',
        'Status': 'Contacted'
    },
    'Sacha': {
        'Phone': '8887884335',
        'Email': 'sacha@gmail.com',
        'Source': 'Referral',
        'Status': 'New'
    },
    'Naira': {
        'Phone': '8759843689',
        'Email': 'naira@gmail.com',
        'Source': 'Cold Call',
        'Status': 'Closed'
    }
}


def add_lead():
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')
    source = input('Source: ')
    status = input('Status: ')
    leads[name] = {
        'Phone': phone,
        'Email': email,
        'Source': source,
        'Status': status
    }
    print(f"{name} added successfully!")


def view_leads():
    for name, details in leads.items():
        print(name, details)


def search_lead():
    search_name = input('Name: ')
    if search_name in leads:
        print(leads[search_name])
    else:
        print('Lead not found')


def update_status():
    name = input('Name: ')
    if name in leads:
        new_status = input('New status: ')
        leads[name]['Status'] = new_status
        print(f"{name}'s status updated to {new_status}")
    else:
        print('Lead not found')


def delete_lead():
    name = input('Name: ')
    if name in leads:
        del leads[name]
        print(f"{name} deleted successfully!")
    else:
        print('Lead not found')


while True:
    print("\n=== Mini CRM ===")
    print("1. Add lead")
    print("2. View all leads")
    print("3. Search lead")
    print("4. Update status")
    print("5. Delete lead")
    print("6. Exit")

    choice = input("Choose: ")

    if choice == '1':
        add_lead()
    elif choice == '2':
        view_leads()
    elif choice == '3':
        search_lead()
    elif choice == '4':
        update_status()
    elif choice == '5':
        delete_lead()
    elif choice == '6':
        print('Exit')
        break
