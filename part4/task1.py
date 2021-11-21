import json
import os.path


def fn_register(log, pwd):
    noreg = True
    with open('data.json', 'r') as file:
        users_data = json.load(file)
    for i in users_data.keys():
        if i == log:
            noreg = False
    if noreg:
        users_data[log] = pwd
        with open('data.json', 'w') as file:
            json.dump(users_data, file) 
    return noreg


def fn_login(log, pwd):
    reg = False
    with open('data.json', 'r') as file:
        users_data = json.load(file)
    for x, y in users_data.items():
        if x == log and y == pwd:
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
    if fn_register(login, passwd):
        print('User is added')
    else:
        print('User is exist')
else:
    if fn_login(login, passwd):
        print('Successful login')
    else:
        print('Login/password incorrected')