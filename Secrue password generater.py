import random
import string
import datetime
adjectives = ['sleepy', 'slow', 'smelly',
 'wet', 'fat', 'red',
 'orange', 'yellow', 'green',
 'blue', 'purple', 'fluffy',
 'white', 'proud', 'brave']
nouns = ['apple', 'dinosaur', 'ball',
 'toaster', 'goat', 'dragon',
 'hammer', 'duck', 'panda',
 'telephone', 'banana', 'teacher']
def p_log(password):
    datetime_object = datetime.datetime.now()
    use=input('your use of this password:')
    with open('password.txt','a', encoding = 'utf-8') as f:
        f.write('\n{} use:{}   passcode: "{}"'.format(datetime_object,use,password))
    print('great! password saved')
def password_g():
    adjective = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    noun = random.choice(nouns)
    noun2 = random.choice(nouns)
    number = random.randrange(0, 100)
    password = adjective + noun + str(number) + adjective2 + noun2
    print('Your new password is: %s \n' % password)
    response = input('Would you like to use this password? Type y or n: \n')
    if response == 'y':
        p_log(password)
    else:
        password_g()

input("\nwelcome to password generater\n")
password_g()
