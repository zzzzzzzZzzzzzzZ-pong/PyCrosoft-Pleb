from time import time
from typing import Text
import webbrowser, datetime

password, incorrectCount = '', 0

def settingUp():
    global password
    while True:
        print('Type a password: ')
        password = input('')
        if password == '':
            print('You need to type something')
        else:
            print('Done!')
            break
    print('This is your password: ' + password)
    print('Restarting...')
settingUp()

for i in range(56):
    print('Restarting...')
while True:
    print('What is the password?')
    ask_password = input('')
    if ask_password == password:
        break    
    elif ask_password != password:
        print('You have to type a password')
        incorrectCount += 1
        if incorrectCount == 12:
            print("You're busted, hacker! You can't log in now! We're locking the account! HAH!")
            break

print("You're logged in")
print('Hello stupid1234')        
today = datetime.date.today()
time = '{today.day}/{today.month}/{today.year}'.format(today=today)
print("The date today is" + time)
while True:
    a_url = input('Type a URL: ')
    print('Redirecting you to ' + a_url)