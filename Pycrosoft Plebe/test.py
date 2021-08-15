password = '1234'
incorrectCount = 0

while True:
    print('What is the password?')
    ask_password = input('')
    if ask_password == password:
        break
        print("You're logged in")
        print('Hello stupid1234')
        today = datetime.date.today()
        time = '{today.day}/{today.month}/{today.year}'.format(today=today)
        print("The date today is" + time)     
    else:
        print('You have to type a password')
        incorrectCount += 1
        if incorrectCount == 12:
            print("You're busted, hacker! You can't log in now!")
            break