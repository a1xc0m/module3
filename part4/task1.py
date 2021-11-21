import json
import os.path

def register(login, passwd):
    noreg = True
    with open('data.json', 'r') as file:
        users_data = json.load(file)
    for i in users_data.keys():
        if i == login:
            noreg = False
    if noreg:
        users_data[login] = passwd
        with open('data.json', 'w') as file:
            json.dump(users_data, file) 
    return noreg

def login_function(login, passwd):
    reg = False
    with open('data.json', 'r') as file:
        users_data = json.load(file)
    for x, y in users_data.items():
        if x == login and y == passwd:
            reg = True      
    return reg

data = {}
if os.path.exists('data.json'):
    print('File exist')
else:
    with open('data.json', 'w') as file:
        json.dump(data, file)
        
select = int(input('0 = Registration, 1 = Door: '))
login = input('Login: ')
passwd = input('Password: ')
if select == 0:
    if register(login, passwd):
        print('User is added')
    else:
        print('User is exist')
else:
    if login_function(login, passwd):
        print('Successful login')
    else:
        print('Login/password incorrected')