import webbrowser
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
    if ask_password != password:
        print('You have to type a password')
        incorrectCount += 1
        if incorrectCount == 12:
            print("You're busted, hacker! You can't log in now!")
            break
    elif ask_password == password:
        break
        print("Welcome! You're logged in!")
        